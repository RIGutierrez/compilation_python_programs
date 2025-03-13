# ask user to input 10 numbers using loop
number = [1,2,3,3,4,5,6,7,7,8,9,9]


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
