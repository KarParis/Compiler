import sys
from antlr4 import *
from oosLexer import oosLexer
from oosParser import oosParser
from oosMyListener import oosMyListener

def main():
    input = FileStream("shape.oos", encoding="utf-8")
    lexer = oosLexer(input)
    stream = CommonTokenStream(lexer)
    parser = oosParser(stream)

    tree = parser.startRule()
    listener = oosMyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print(listener.get_output())

    

if __name__ == "__main__":
    main()