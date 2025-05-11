# Borrowed from the ANTLR docs:
# https://github.com/antlr/antlr4/blob/master/doc/python-target.md

import argparse
from pathlib import Path
import sys
import os
import subprocess

from antlr4 import FileStream, CommonTokenStream
from .parser.SnailLexer import SnailLexer
from .parser.SnailParser import SnailParser
from .symbols import SymbolTable
from .interpreter import Interpreter
from .compiler import Compiler

argparser = argparse.ArgumentParser(description="Snail language driver")
argparser.add_argument("-i", "--interpret", action="store_true", dest = "interpret")
argparser.add_argument("-c", "--compile", action="store_true", dest = "compile")
argparser.add_argument(dest = "filename", metavar="filename")
args = argparser.parse_args()

def main():
    input_stream = FileStream(args.filename)
    lexer = SnailLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnailParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors")
        sys.exit(1)

    if args.compile:
        symbols = SymbolTable()
        compiler = Compiler(symbols)
        try:
            module = compiler.visit(tree)
            print(module)
            if Path("snail.ll").exists():
                os.remove("snail.ll")
            else:
                with open("snail.ll", "wt") as out:
                    out.write(str(module))
                subprocess.run(["clang", "snail.ll", "-w", "-o", "snail"])

        except ValueError as e:
            print(e)
            sys.exit(68) # ;)

    if args.interpret:
        symbols = SymbolTable()
        interpreter = Interpreter(symbols)
        try:
            interpreter.visit(tree)

        except ValueError as e:
            print(e)
            sys.exit(68)

if __name__ == '__main__':
    main()
