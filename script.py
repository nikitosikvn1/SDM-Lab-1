import sys
import os
from math import sqrt

from colors import RED, GREEN, YELLOW, RESET

args = sys.argv[1:]
num_of_args = len(args)

if num_of_args == 0:
    numbers, labels = [], ["a", "b", "c"]

    while len(numbers) < 3:
        user_input = input(YELLOW + f"Enter {labels[len(numbers)]}: " + RESET)
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print(RED + "Error. Expected a valid real number, got invalid instead" + RESET)

    a, b, c = numbers

elif num_of_args == 1:
    if os.path.isfile(args[0]):
        with open(args[0], 'r') as file:
            first_line = file.readline()
            try:
                a, b, c = map(float, first_line.split())
            except ValueError:
                print(RED + "Error. File contains invalid data" + RESET)
                sys.exit()
    else:
        print(RED + "Error. It looks like the argument passed is not a path to a file" + RESET)
        sys.exit()

else:
    print(RED + "Invalid number of arguments." + RESET)
    sys.exit()

print(f"Equation is: {a}x^2 + {b}x + {c} = 0")

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print("There are 0 roots")

elif discriminant == 0:
    x = -b / (2 * a)
    print("There is 1 root")
    print(GREEN + f"x = {x}" + RESET)

else:
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)
    print("There are 2 roots")
    print(GREEN + f"x1 = {x1}" + RESET)
    print(GREEN + f"x2 = {x2}" + RESET)
