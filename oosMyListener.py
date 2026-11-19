from antlr4 import *
from oosListener import oosListener
from oosParser import oosParser

class oosMyListener(oosListener):

    def __init__(self):
        self.output = []
        self.tabs = 0

        self.current_class = None
        self.current_method = None
        self.in_constructor = False
        self.in_method = False

        self.return_type = None
        self.current_assignment = None
        self.current_prefix = None

        #counter for class constructors
        self.constructor_counter = 0

        #current class methods
        self.method_counts = {}

        self.symbol_table = {
            "classes": {}, 
            "local": {}
        }

        self.c_code = {}

    def add_tab(self):
        self.tabs += 1

    def remove_tab(self):
        self.tabs -= 1

    def add_output(self, text):
        self.output.append("\t" * self.tabs + text)

    def get_output(self):
        return "\n".join(self.output)



#--------------- MY LISTENER ---------------

    #Start Rule
    def enterStartRule(self, ctx: oosParser.StartRuleContext):
        print("Entering of Start Rule")
        self.add_output("\n//------------------------ Code in C ------------------------//")
        self.add_output("\n#include <stdio.h>")
        self.add_output("#include <stdlib.h>")
        self.add_output("")

    def exitStartRule(self, ctx: oosParser.StartRuleContext):
        print("Exiting Start Rule")
        with open("output.c", "w") as f:
            f.write(self.get_output())



    #Classes    
    def enterClasses(self, ctx: oosParser.ClassesContext):
        print("Entering Classes")

    def exitClasses(self, ctx: oosParser.ClassesContext):
        print("Exiting Classes")



    #Class def
    def enterClass_def(self, ctx: oosParser.Class_defContext):
        print(f"Entering Class Definition : {self.current_class}")
        class_name = ctx.class_name(0).getText()
        self.current_class = class_name

        self.symbol_table["classes"][class_name] = {
            "parents": [],
            "fields": {},
            "constructors": [],
            "methods": {}
        }
        
        self.add_output("typedef struct " + self.current_class + "{")
        self.add_tab()

        all_classes = ctx.class_name()
        if len(all_classes) > 1:
            cur_info = self.symbol_table["classes"][class_name]
            for parent in all_classes[1:]:
                parent_name = parent.getText()
                cur_info["parents"].append(parent_name)

                #get parent fields and methods
                if parent_name in self.symbol_table["classes"]:
                    parent_fields = self.symbol_table["classes"][parent_name]["fields"]
                    parent_methods = self.symbol_table["classes"][parent_name]["methods"]
                else:
                    parent_fields = {}
                    parent_methods = {}

                for field_name, field_type in parent_fields.items():
                    if field_name not in cur_info["fields"]:
                        cur_info["fields"][field_name] = field_type
                        if field_type == "int":
                            self.add_output(f"int {field_name};")
                        else:
                            self.add_output(f"struct {field_type}* {field_name};")

                for method_name, parent_class in parent_methods.items():
                    if method_name not in cur_info["methods"]:
                        cur_info["methods"][method_name] = parent_class


    def exitClass_def(self, ctx: oosParser.Class_defContext):
        print(f"Exiting Class Definition : {self.current_class}\n")
        self.current_class = None



    #Class main def
    def enterClass_main_def(self, ctx: oosParser.Class_main_defContext):
        self.current_class = "main"
        print(f"Entering Main Class Definition : {self.current_class}")
        self.add_output("int main(){")
        self.add_tab()

    def exitClass_main_def(self, ctx: oosParser.Class_main_defContext):
        print(f"Exiting Main Class Definition : {self.current_class}\n")
        self.add_output("")
        self.add_output("return 0;")
        self.remove_tab()
        self.add_output("}")
        self.current_class = None



    #Class name 
    def enterClass_name(self, ctx: oosParser.Class_nameContext):
        print("Entering Class Name")

    def exitClass_name(self, ctx: oosParser.Class_nameContext):
        print("Exiting Class Name")



    #Declarations
    def enterDeclarations(self, ctx: oosParser.DeclarationsContext):
        print("Entering Declarations")

    def exitDeclarations(self, ctx: oosParser.DeclarationsContext):
        print("Exiting Declarations")



    #Class Body
    def enterClass_body(self, ctx: oosParser.Class_bodyContext):
        print("Entering Class Body")
        self.remove_tab()
        self.output.append(f"}} {self.current_class};")
        self.add_output("")
        self.constructor_counter = 0
        self.method_counts = {}

    def exitClass_body(self, ctx: oosParser.Class_bodyContext):
        print("Exiting Class Body")



    #Main Body
    def enterMain_body(self, ctx: oosParser.Main_bodyContext):
        print("Entering Main Body")

    def exitMain_body(self, ctx: oosParser.Main_bodyContext):
        print("Exiting Main Body")



    #Decl_line
    def enterDecl_line(self, ctx:oosParser.Decl_lineContext):
        print("Entering Decl_line")
        raw_var_type = ctx.types().getText()
        var_type = raw_var_type
        add_star = False

        #not int type
        if var_type != "int":
            var_type = f"struct {var_type}*"
            add_star = True

        ids = []
        for id in ctx.ID():
            var_name = id.getText()
            #local variable
            if self.in_method or self.current_class == "main":
                self.symbol_table["local"][var_name] = raw_var_type
                ids.append(var_name)
            #class field
            else:
                if var_name not in self.symbol_table["classes"][self.current_class]["fields"]:
                    self.symbol_table["classes"][self.current_class]["fields"][var_name] = raw_var_type
                    ids.append(var_name)

        if len(ids) == 0:
            return

        #multiple pointers at the same line
        if len(ids) > 1 and add_star:
            types_str = var_type.replace("*" , "")
            for name in ids:
                names_str = ", ".join(f"*{name}")
            decl_str = f"{types_str} {names_str};"

        #multiple variables at the same line
        if len(ids) > 1:
            names_str = ", ".join(ids)
            decl_str = f"{var_type} {names_str};"
        else:
            decl_str = f"{var_type} {ids[0]};"


        if self.in_method or self.in_constructor:
            self.add_output(decl_str)
        elif self.current_class is not None:
            self.add_output(decl_str)
            
        
                  
    def exitDecl_line(self, ctx: oosParser.Decl_lineContext):
        print("Exiting Decl_line")
        #self.add_output("")



    #Constructor Def
    def enterConstructor_def(self, ctx: oosParser.Constructor_defContext):
        print("Entering Constructor Definition")
        self.in_constructor = True
        self.in_method = True

        #clear local variables
        self.symbol_table["local"].clear()

        if ctx.class_name():
            class_name = ctx.class_name().ID().getText()
            self.constructor_counter += 1
            if self.constructor_counter == 1:
                constructor_name = f"{class_name}_init"
            else:
                constructor_name = f"{class_name}_init_{self.constructor_counter}"
                
            self.current_method = constructor_name
        
        else:
           print("Class does not have a construtor")
           exit(0) 

    def exitConstructor_def(self, ctx: oosParser.Constructor_defContext):
        print("Exiting Constructor Definition")
        self.add_output("return self;")
        self.remove_tab()
        self.add_output("}")
        self.add_output("")
        self.in_constructor = False
        self.in_method = False



    #Method def
    def enterMethod_def(self, ctx: oosParser.Method_defContext):
        print("Entering Method Definition")
        self.in_method = True

        #clear local varibles
        self.symbol_table["local"].clear()

        method_name = ctx.ID().getText()
        self.symbol_table["classes"][self.current_class]["methods"][method_name] = self.current_class
        
        #add method counter 0
        if method_name not in self.method_counts:
            self.method_counts[method_name] = 1
        else:
            self.method_counts[method_name] += 1

        #if a method name appears more than once, change name
        if self.method_counts[method_name] == 1:
            self.current_method = f"{self.current_class}_{method_name}"
        else:
            self.current_method = f"{self.current_class}_{method_name}_{self.method_counts[method_name]}"
            

        if ctx.class_name():
            self.return_type = f"struct {ctx.class_name().getText()}*"
        else:
            child_text = ctx.getChild(4).getText()
            if child_text == "int":
                self.return_type = "int"
            else:
                self.return_type = "void"

    def exitMethod_def(self, ctx: oosParser.Method_defContext):
        print("Exiting Method Definition")
        self.remove_tab()
        self.add_output("}")
        self.add_output("")
        self.current_method = None
        self.in_method = False



    #Method Main Def
    def enterMethod_main_def(self, ctx: oosParser.Method_main_defContext):
        print("Entering Method Main Definition")
        self.in_method = True
        self.current_method = "main"

        #clear local variables
       # self.symbol_table["local"].clear()
        
    def exitMethod_main_def(self, ctx: oosParser.Method_main_defContext):
        print("Exiting Method Main Definition")
        self.current_method = None
        self.in_method = False



    #Types
    def enterTypes(self, ctx: oosParser.TypesContext):
        print("Entering Types")

    def exitTypes(self, ctx: oosParser.TypesContext):
        print("Exiting Types")



    #Parameters
    def enterParameters(self, ctx: oosParser.ParametersContext):
        print("Entering Parameters")

    def exitParameters(self, ctx: oosParser.ParametersContext):
        print("Exiting Parameters")



    #Method Body
    def enterMethod_body(self, ctx: oosParser.Method_bodyContext):
        print("Entering Method Body")

    def exitMethod_body(self, ctx: oosParser.Method_bodyContext):
        print("Exiting Method Body")



    #Return Type
    def enterReturn_type(self, ctx: oosParser.Return_typeContext):
        print("Entering Return Type")

    def exitReturn_type(self, ctx: oosParser.Return_typeContext):
        print("Exiting Return Type")



    #Parlist
    def enterParlist(self, ctx: oosParser.ParlistContext):
        print("Entering Parlist")
        parameters = [f"struct {self.current_class}* self"]
        ids = ctx.ID()
        types = ctx.types()

        if ids and types:
            for i in range(len(ids)):
                param_type = types[i].getText()
                param_name = ids[i].getText()
                self.symbol_table["local"][param_name] = param_type
                parameters.append(f"{param_type} {param_name}")

        params = ", ".join(parameters)
        if self.in_constructor:
            self.add_output(f"{self.current_class}* {self.current_method}({params}) {{")
            self.add_tab()
            self.add_output("if (self == NULL) {")
            self.add_tab()
            self.add_output(f"self = (struct {self.current_class}*) malloc(sizeof(struct {self.current_class}));")
            self.remove_tab()
            self.add_output("}")
            self.add_output("")
        else:
            self.add_output(f"{self.return_type} {self.current_method}({params}) {{")
            self.add_tab()

    def exitParlist(self, ctx: oosParser.ParlistContext):
        print("Exiting Parlist")



    #Statements
    def enterStatements(self, ctx: oosParser.StatementsContext):
        print("Entering Statements")

    def exitStatements(self, ctx: oosParser.StatementsContext):
        print("Exiting Statements")



    #Statement
    def enterStatement(self, ctx: oosParser.StatementContext):
        print("Entering Statement")

    def exitStatement(self, ctx: oosParser.StatementContext):
        print("Exiting Statement")



    #Assignment Statement
    def enterAssignment_stat(self, ctx: oosParser.Assignment_statContext):
        print("Entering Assignment Statement")
        if ctx.ID():
            name = ctx.ID().getText()
            if ctx.getChild(0).getText() == "self.":
                self.current_assignment = f"self->{name}"
            else:
                self.current_assignment = name

    def exitAssignment_stat(self, ctx: oosParser.Assignment_statContext):
        print("Exiting Assignment Statement")
        if ctx.expression():
            expr_code = self.c_code[ctx.expression()]
            self.add_output(f"{self.current_assignment} = {expr_code};")
        self.current_assignment = None

    
    #Direct Call Statement
    def enterDirect_call_stat(self, ctx: oosParser.Direct_call_statContext):
        print("Entering Direct Call Statement")
                       
    def exitDirect_call_stat(self, ctx: oosParser.Direct_call_statContext):
        print("Exiting Direct Call Statement")

        func_name = ctx.func_call().ID().getText()
        arg_code = []
        arglist = ctx.func_call().arguments().arglist()
        if arglist and arglist.argitem():
            for item in arglist.argitem():
                arg_code.append(self.c_code[item.expression()])

        if ctx.ID():
            obj_name = ctx.ID().getText()
            #self.obj().function()
            if ctx.getChild(0).getText() == "self.":
                obj_c = f"self->{obj_name}"
                obj_class = self.symbol_table["classes"][self.current_class]["fields"][obj_name]
            
            #obj().function
            else:
                obj_c = obj_name
                obj_class = self.symbol_table["local"][obj_name]

        #self.function()
        else:
            obj_c = "self"
            obj_class = self.current_class

        owner_class = self.symbol_table["classes"][obj_class]["methods"].get(func_name, obj_class)
        if owner_class != obj_class:
            obj_c = f"(struct {owner_class}*){obj_c}"

        all_args = ", ".join([obj_c] + arg_code)
        self.add_output(f"{obj_class}_{func_name}({all_args})")


    #If Statement
    def enterIf_stat(self, ctx: oosParser.If_statContext):
        print("Entering If Statement")
        cond = ctx.condition().getText().replace("self.", "self->")
        self.add_output(f"if ({cond}) {{")
        self.add_tab()

    def exitIf_stat(self, ctx: oosParser.If_statContext):
        print("Exiting If Statement")
        self.remove_tab()
        self.add_output("}")


    #Else Part
    def enterElse_part(self, ctx: oosParser.Else_partContext):
        print("Entering Else Part")
        if ctx.getChildCount() > 0:
            self.remove_tab()
            self.add_output("} else {")
            self.add_tab()

    def exitElse_part(self, ctx: oosParser.Else_partContext):
        print("Exiting Else Part")
    


    #While Statement
    def enterWhile_stat(self, ctx: oosParser.While_statContext):
        print("Entering While Statement")
        cond = ctx.condition().getText().replace("self.", "self->")
        self.add_output(f"while ({cond}) {{")
        self.add_tab()

    def exitWhile_stat(self , ctx: oosParser.While_statContext):
        print("Exiting While Statement")
        self.remove_tab()
        self.add_output("}")


    #Return Statement
    def enterReturn_stat(self, ctx: oosParser.Return_statContext):
        print("Entering Return Statement")

    def exitReturn_stat(self, ctx: oosParser.Return_statContext):
        print("Exiting Return Statement")
        if ctx.expression():
            self.add_output(f"return {self.c_code[ctx.expression()]};")
        elif ctx.ID():
            var_name = ctx.ID().getText()
            self.add_output(f"return self->{var_name};")
        else:
            self.add_output("return self;")
        
        
    #Input Statement
    def enterInput_stat(self, ctx: oosParser.Input_statContext):
        print("Entering Input Statement")

        if ctx.ID():
            var_name = ctx.ID().getText()
        else:
            var_name = ""

        if "self" in ctx.getText():
            self.add_output(f"scanf(\"%d\", &self -> {var_name});")
        else:
            self.add_output(f"scanf(\"%d\", &{var_name});")

    def exitInput_stat(self, ctx: oosParser.Input_statContext):
        print("Exiting Input Statement")


    #Print Statement
    def enterPrint_stat(self, ctx: oosParser.Print_statContext):
        print("Entering Print Statement")

    def exitPrint_stat(self, ctx: oosParser.Print_statContext):
        print("Exiting Print Statement")
        num_of_expr = len(ctx.expression())
        text = ", ".join(["%d"] * num_of_expr)

        args_list =[]
        for exp in ctx.expression():
            args_list.append(self.c_code[exp])
        args = ", ".join(args_list)
        self.add_output(f'printf("{text}\\n", {args});')

    #Expression 
    def enterExpression(self, ctx: oosParser.ExpressionContext):
        print("Entering Expression")

    def exitExpression(self, ctx: oosParser.ExpressionContext):
        print("Exiting Expression")
        res = ""
        if ctx.optional_sign() and ctx.optional_sign().getText():
            res += ctx.optional_sign().getText()

        terms = ctx.term()
        add_opers = ctx.add_oper()
        res += self.c_code[terms[0]]
        for i in range(1, len(terms)):
            res += f"{add_opers[i-1].getText()} {self.c_code[terms[i]]}"

        self.c_code[ctx] = res

    #Arguments
    def enterArgument(self, ctc: oosParser.ArgumentsContext):
        print("Entering Arguments")

    def exitArguments(self, ctx: oosParser.ArgumentsContext):
        print("Exiting Arguments")

    #Condition
    def enterCondition(self, ctx: oosParser.ConditionContext):
        print("Entering Condition")

    def exitCondition(self, ctx: oosParser.ConditionContext):
        print("Exiting Condition")

    #Optional Sign
    def enterOptional_sign(self, ctx: oosParser.Optional_signContext):
        print("Entering Optional Sign")

    def exitOptional_sign(self, ctx: oosParser.Optional_signContext):
        print("Exiting Optional Sign")

    #Term
    def enterTerm(self, ctx: oosParser.TermContext):
        print("Entering Term")

    def exitTerm(self, ctx: oosParser.TermContext):
        print("Exiting Term")
        factors = ctx.factor()
        mul_opers = ctx.mul_oper()
        res = self.c_code[factors[0]]

        for i in range(1, len(factors)):
            res += f"{mul_opers[i-1].getText()} {self.c_code[factors[i]]}"

        self.c_code[ctx] = res
        
    #Add Operator
    def enterAdd_oper(self, ctx: oosParser.Add_operContext):
        print("Entering Add Operator")
        
    def exitAdd_oper(self, ctx: oosParser.Add_operContext):
        print("Exiting Add Operator")


    #ArgList
    def enterArglist(self, ctx: oosParser.ArglistContext):
        print("Entering Arglist")

    def exitArglist(self, ctx: oosParser.ArglistContext):
        print("Exiting Arglist")

    #Boolterm
    def enterBoolterm(self, ctx: oosParser.BooltermContext):
        print("Entering Boolterm")

    def exitBoolterm(self, ctx: oosParser.BooltermContext):
        print("Exiting Boolterm")


    #Factor
    def enterFactor(self, ctx: oosParser.FactorContext):
        print("Entering Factor")

    def exitFactor(self, ctx: oosParser.FactorContext):
        print("Exiting Factor")

        # INTEGER
        if ctx.INTEGER():
            self.c_code[ctx] = ctx.INTEGER().getText()

        # '(' expression ')'
        elif ctx.expression():
            self.c_code[ctx] = f"({self.c_code[ctx.expression()]})"

        # func_call
        elif ctx.func_call():
            func_name = ctx.func_call().ID().getText()
            arg_code = []
            arglist = ctx.func_call().arguments().arglist()
            if arglist and arglist.argitem():
                for item in arglist.argitem():
                    arg_code.append(self.c_code[item.expression()])

            if ctx.ID():
                obj_name = ctx.ID(0).getText()

                #yparxei antikeimeno self.obj().function()
                if ctx.getChild(0).getText() == "self.":
                    obj_c = f"self->{obj_name}"
                    obj_class = self.symbol_table["classes"][self.current_class]["fields"][obj_name]
                #antikeimeno obj().function()
                else:
                    obj_c = obj_name
                    obj_class = self.symbol_table["local"][obj_name]

                owner_class = self.symbol_table["classes"][obj_class]["methods"].get(func_name, obj_class)
                if owner_class != obj_class:
                    obj_c = f"(struct {owner_class}*){obj_c}"

                all_args = ", ".join([obj_c] + arg_code)
                self.c_code[ctx] = f"{obj_class}_{func_name}({all_args})"


            # Constructor call
            elif ctx.getChild(0).getText() != "self." and func_name in self.symbol_table["classes"]:
                all_args = ", ".join(["NULL"] + arg_code)
                self.c_code[ctx] = f"{func_name}_init({all_args})"

            # self method 
            else:
                owner_class = self.symbol_table["classes"][self.current_class]["methods"].get(func_name, self.current_class)
                if owner_class != self.current_class:
                    first_arg = f"(struct {owner_class}*)self"
                else:
                    first_arg = "self"

                all_args = ", ".join([first_arg] + arg_code)
                self.c_code[ctx] = f"{owner_class}_{func_name}({all_args})"
            

        # ID '.' ID
        elif len(ctx.ID()) == 2:
            obj_name = ctx.ID(0).getText()
            field_name = ctx.ID(1).getText()
            self.c_code[ctx] = f"{obj_name}->{field_name}"

        # ('self.')?ID
        elif len(ctx.ID()) == 1 and not ctx.func_call():
            var_name = ctx.ID(0).getText()
            if ctx.getChild(0).getText() == "self.":
                self.c_code[ctx] = f"self->{var_name}"
            else:
                self.c_code[ctx] = var_name

    
    #Mul oper
    def enterMul_oper(self, ctx: oosParser.Mul_operContext):
        print("Entering Mul Operator")

    def exitMul_oper(self, ctx: oosParser.Mul_operContext):
        print("Exiting Mul Operator")

    #Argitem
    def enterArgitem(self, ctx: oosParser.ArgitemContext):
        print("Entering Argitem")

    def exitArgitem(self, ctx: oosParser.ArgitemContext):
        print("Exiting Argitem")

    #Boolfactor
    def enterBoolfactor(self, ctx: oosParser.BoolfactorContext):
        print("Entering Boolfactor")

    def exitBoolfactor(self, ctx: oosParser.BoolfactorContext):
        print("Exiting Boolfactor")

    #Func_call
    def enterFunc_call(self, ctx: oosParser.Func_callContext):
        print("Entering Func Call")

    def exitFunc_call(self, ctx: oosParser.Func_callContext):
        print("Exiting Func Call")

    #Constructor call   
    def enterConstructor_call(self, ctx: oosParser.Constructor_callContext):
        print("Entering Constructor Call")

    def exitConstructor_call(self, ctx: oosParser.Constructor_callContext):
        print("Exiting Constructor Call")

    #Rel_oper
    def enterRel_oper(self, ctx: oosParser.Rel_operContext):
        print("Entering Rel_Oper")
    
    def exitRel_oper(self, ctx: oosParser.Rel_operContext):
        print("Exiting Rel_Oper")