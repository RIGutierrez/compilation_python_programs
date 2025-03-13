# list to store value
numbers = []

while True:
    try:
        # ask user to input number
        number = int(input("Please input a number: "))

        # checking if number is in numbers (list)
        if number in numbers:
            print("Duplicate")
        else:
            print("Unique")
            
    # program break if invalid input
    except ValueError:
        break




