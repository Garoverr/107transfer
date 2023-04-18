#!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## 107transfer
## File description:
## python file
##

from argparse import ArgumentParser, Namespace
from sys import argv, exit
from typing import List


def man_help() -> int:
    print(
        """USAGE
    ./107transfer [num dem]*
DESCRIPTION
    num     polynomial numerator defined by its coefficients
    dem     polynomial denominator defined by its coefficients

    2x -h for more infos.    """
    )
    return 0


def man_help2() -> int:
    print(
        """USAGE
    ./107transfer [num dem]*
DESCRIPTION
    num     polynomial numerator defined by its coefficients, separated by '*'
            Example: "1*2*3" for "3x^2 + 2x + 1"
    dem     polynomial denominator defined by its coefficients, separated by '*'
            Example: "1*2*3" for "3x^2 + 2x + 1"
            Coefficients should not be zero.
            Coefficients must be integers between -100 and 100 inclusive."""
    )
    return 0


def get_polynom(formule: str) -> List[int]:
    try:
        return [int(coeff) for coeff in formule.split('*')]
    except ValueError:
        print("Invalid Number")
        exit(84)


def evaluate_polynomial(coefficients: List[int], x: float) -> float:
    result = 0.0
    for coeff in reversed(coefficients):
        result = result * x + coeff
    return result


def trans_print(args: List[List[int]]) -> None:
    x: float = 0
    while x <= 1.001:
        result: float = 1
        for num, dem in zip(args[::2], args[1::2]):
            numerator = evaluate_polynomial(num, x)
            denominator = evaluate_polynomial(dem, x)
            if denominator == 0:
                exit(84)
            result *= numerator / denominator
        print(f"{x:.3f} -> {result:.5f}")
        x += 0.001


def get_args() -> List[List[int]]:
    parser: ArgumentParser = ArgumentParser()
    parse_list: List[List[int]] = []

    parser.add_argument("formules", type=str, nargs="+")

    try:
        args: Namespace = parser.parse_args()
        parse_list = [get_polynom(formule) for formule in args.formules]
    except SystemExit:
        exit(84)

    return parse_list


def main() -> int:
    if "-h" in argv:
        if argv.count("-h") == 2:
            return man_help2()
        return man_help()
    if (len(argv) - 1) % 2 != 0:
        print("Invalid Numbers")
        return 84
    args: List[List[int]] = get_args()
    trans_print(args)
    return 0


if __name__ == "__main__":
    exit(main())
