# list to store value
numbers = []

# ask user to input numbers using loop
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# new list for inputs unique numbers
unique_numbers = []

# remove duplicates and print only the first entry
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

        # print numbers
        print(num)