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

if numbers:
    # count frequency of number inputted
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
            print(num)

# find most frequent number inputted
# print most frequent and how many times appeared