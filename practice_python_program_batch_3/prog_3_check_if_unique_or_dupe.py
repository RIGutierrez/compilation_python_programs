# list to store value
numbers = []

# ask user to input number
for i in range(10):
    number = int(input(f"Please input a number {i + 1}: ")) 
    if number in numbers:
        print("Duplicate")
    else:
        print("Unique")
        numbers.append(number)
    






# program break if invalid input

