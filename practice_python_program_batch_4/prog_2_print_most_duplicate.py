# list to store value
numbers = []

while True:
    try:

        # ask user to input number
        number = int(input("Please input a number: "))
        numbers.append(number)
    except ValueError:
        print("Invalid input")
        break



# count frequency of number inputted
# find most frequent number inputted
# print most frequent and how many times appeared