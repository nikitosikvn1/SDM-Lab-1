import sys

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
    pass
# If more than one argument was passed, then the error output
else:
    print("Invalid number of arguments.")
    sys.exit()
