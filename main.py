from typing import *
from solution import question
from utils import TreeNode, ListNode, build_tree
from collections import *
import inspect
import time
import ast
import sys

sys.setrecursionlimit(2000)  # increase recursion limit for deep trees

def parse_input(input_string: str, args: dict) -> List[List[int|str|None]]: 
    """
    Based on the input number to parse the input string,
        and convert it to list of test cases
    Parameters
    ----------
    input_string: str
        The input string from the problem statement
    args: dict
        The arguments of the function

    Returns
    -------
    input_tests: list
        The list of test cases

    """

    args = list(args.values())
    arg_num = len(args)
    input_lines = input_string.strip().split('\n')
    assert len(input_lines) % arg_num == 0, "Input string does not match the number of arguments"
    input_lines = [input_lines[i:i+arg_num] for i in range(0, len(input_lines), arg_num)]
    input_tests = []
    for i, input_line_per_test in enumerate(input_lines):
        input_test = []
        for j, arg in enumerate(args):
            if arg.annotation == int:
                input_test.append(int(input_line_per_test[j]))
            elif arg.annotation == str:
                # remove the leading and trailing quotes
                # find the first and last quote
                first_quote = input_line_per_test[j].find('"')
                last_quote = input_line_per_test[j].rfind('"')
                if first_quote != -1 and last_quote != -1:
                    input_test.append(input_line_per_test[j][first_quote+1:last_quote])
                else:
                    raise ValueError(f"Invalid string input: {input_line_per_test[j]}")
            elif arg.annotation == Optional[TreeNode]:
                input_test.append(build_tree(input_line_per_test[j]))
            elif arg.annotation == Optional[ListNode]:
                input_test.append(ListNode.of(ast.literal_eval(input_line_per_test[j])))
            elif arg.annotation.__origin__ == list:
                input_test.append(ast.literal_eval(input_line_per_test[j]))
            elif arg.annotation == None:
                input_test.append(None)
            else:
                raise TypeError(f"Unsupported argument type: {arg.annotation}")
        input_tests.append(input_test)
    return input_tests

def format_str(data: Any, ) -> str:
    """
    Format the data to a string
    
    Parameters
    ----------
    data: Any
        The data to be formatted

    Returns
    -------
    result: str
        The formatted string
    """

    # If the result is None, convert it to '[]'
    if data is None:
        result_str = "[]"
    elif isinstance(data, bool):
        if data:
            result_str = "true"
        else:
            result_str = "false"
    elif isinstance(data, str):
        result_str = '"' + data + '"'
    else:
        result_str = str(data)

    if len(result_str) > 100:
        result_str = result_str[:100] + "..."
    return result_str

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_string = file.read()

    # get the input arguments for Solution
    args = inspect.signature(question).parameters
    input_tests = parse_input(input_string, args)

    for i, input_test in enumerate(input_tests):
        print("Input test number: ", i)
        print("Input arguments: ")
        for i, arg in enumerate(input_test):
            print(f"\targ{i} :", format_str(arg))

        # call the function with the input test
        # measure the time taken to run the function
        start_time = time.time()
        result = question(*input_test)
        end_time = time.time()

        print("[Result] ", format_str(result))
        print("[Cost]", f"{(end_time - start_time) * 1000:.3f} ms")
        print("-" * 50)
