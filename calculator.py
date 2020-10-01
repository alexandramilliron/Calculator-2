"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)


def calculator():
    problem = ""
    while problem != "q":
        problem = input("Enter your equation > ")
        problemsplit = problem.split(' ')
        operator = problemsplit[0]
       
        if operator == "add" or operator == "+":
            num1 = float(problemsplit[1])
            num2 = float(problemsplit[2])
            print(add(num1, num2))

        elif operator == "subtract" or operator == "-":
            num1 = float(problemsplit[1])
            num2 = float(problemsplit[2])
            print(subtract(num1, num2))

        elif operator == "power" or operator == "**":
            num1 = float(problemsplit[1])
            num2 = float(problemsplit[2])
            print(power(num1, num2))

        elif operator == "multiply" or operator == "*":
            num1 = float(problemsplit[1])
            num2 = float(problemsplit[2])
            print(multiply(num1, num2))

        elif operator == "%" or operator == "mod":
            num1 = float(problemsplit[1])
            num2 = float(problemsplit[2])
            print(mod(num1, num2))

        elif operator == "divide" or operator == "/":
            num1 = float(problemsplit[1])
            num2 = float(problemsplit[2])
            print(divide(num1, num2))

        elif operator == "square":
            num1 = float(problemsplit[1])
            print(square(num1))

        elif operator == "cube":
            num1 = float(problemsplit[1])
            print(cube(num1))
calculator()



