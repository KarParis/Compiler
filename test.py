import sys
from antlr4 import *
from oosLexer import oosLexer
from oosParser import oosParser
from oosMyListener import oosMyListener

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 oosCompiler.py <testfile.oos>")
        sys.exit(1)

    input_file = sys.argv[1]
    input = FileStream(input_file, encoding="utf-8")
    lexer = oosLexer(input)
    stream = CommonTokenStream(lexer)
    parser = oosParser(stream)

    tree = parser.startRule()
    listener = oosMyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print("Created output.c")
    print("Created states.txt")
    

if __name__ == "__main__":
    main()