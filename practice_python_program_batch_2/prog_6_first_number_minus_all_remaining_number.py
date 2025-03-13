# ask user to input for first number (starting value)
inputs = int(input("Enter Number 1: "))

# initialize result
result = inputs

# loop for asking input 
for i in range(9):
    numbers = int(input(f"Enter Number {i + 2}: "))

    # subtract
    result -= numbers
   
# print result
print(f"The result is: {result}")