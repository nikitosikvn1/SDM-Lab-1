import sys
import os

args = sys.argv[1:]
numOfArgs = len(args)

# If no arguments were passed, then use interactive mode
if numOfArgs == 0:
    numbers, labels = [], ["a", "b", "c"]

    while len(numbers) < 3:
        user_input = input(f"Enter {labels[len(numbers)]}: ")
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Error. Expected a valid real number, got invalid instead")

    a, b, c = numbers
# If one argument was passed, then check if it is a path to a file and use file mode
elif numOfArgs == 1:
    if os.path.isfile(args[0]):
        with open(args[0], 'r') as file:
            first_line = file.readline()
            try:
                a, b, c = map(float, first_line.split())
            except ValueError:
                print("Error. File contains invalid data")
                sys.exit()
    else:
        print("It looks like the argument passed is not a path to a file.")
# If more than one argument was passed, then the error output
else:
    print("Invalid number of arguments.")
    sys.exit()
