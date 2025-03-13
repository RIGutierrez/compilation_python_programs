# ask user to input 10 numbers using loop
for number in range(10):
    number = int(input(f"Enter number {number + 1}: "))

# new list for input appear only once
unique_number = []
duplicate_number = []

for element in number:
    if element not in unique_number:
        unique_number.append(element)
    elif element not in duplicate_number:
        duplicate_number.append(element)    
# print no duplicate 

print(unique_number)
print(duplicate_number)