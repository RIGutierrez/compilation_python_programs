# list to store value
numbers = []

while True:
    try:

        # ask user to input numbers
        number = int(input("Please input a number: "))

        # store number to numbers
        numbers.append(number)
    except ValueError:
        break


# break if invalid
# check lowest number