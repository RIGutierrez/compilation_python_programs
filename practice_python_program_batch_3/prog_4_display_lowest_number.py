# list to store value
numbers = []

while True:
    try:

        # ask user to input numbers
        number = int(input("Please input a number: "))

        # store number to numbers
        numbers.append(number)

    # break if invalid
    except ValueError:
        break

# check lowest number   
if numbers: 
    print(min(numbers))

