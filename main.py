from typing import *
from solution import question
from collections import *
from tester import Tester
import sys

sys.setrecursionlimit(2000)  # increase recursion limit for deep trees

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_string = file.read()

        # Instantiate and run the Tester class
        tester = Tester(input_string, question)
        tester.run_tests()
