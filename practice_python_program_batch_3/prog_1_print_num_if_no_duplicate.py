# list to store inputs
numbers = []

# ask user to input 10 numbers using loop
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# new list for input appear unique and duplicate
unique_number = []
duplicate_number = []

for element in numbers:
    if element not in unique_number:
        unique_number.append(element)
    elif element not in duplicate_number:
        duplicate_number.append(element)    

# print no duplicate 
print("Numbers with no duplicates: ")
for number in unique_number:
    if number not in duplicate_number:
        print(number)