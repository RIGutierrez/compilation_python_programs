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
            
# find most frequent number inputted
    count = 0
    most_frequent = []
    for num in frequency:
        if frequency[num] > count:
            count = frequency[num]
            most_frequent = [num]
        elif frequency[num] == count:
            most_frequent.append(num)

# print most frequent and how many times appeared
    print(f"Most duplicates: {most_frequent}")
    print(f"Appeared: [{count}] times")