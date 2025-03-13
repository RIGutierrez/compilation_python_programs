# initialize counter for odd num
odd_count = 0

for i in range(10):
    # ask user to input a number
    number = int(input(f"Please Enter Number {i + 1}: "))

    # check if the number inputted is odd
    if number % 2 != 0:
        # increment count if odd
        odd_count += 1

# print the count of odd numbers        
print(f"The number of odd numbers is: {odd_count}")