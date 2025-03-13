# initialize variable to store sum of all 10 numbers
total = 0

for i in range(10):
    # ask user to input 10 numbers 
    number = float(input(f"Please Enter Number {i + 1}: "))

    # add the current number to the total sum
    total += number
    
# print the total sum
print(f"The sum of all 10 numbers is: {total}")