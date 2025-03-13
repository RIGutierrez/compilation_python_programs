# initialize counter for even number
even_count = 0

for i in range(10):
    # ask user to input a number
    number = float(input(f"Please Enter Number {i + 1}: "))

    # check if the number inputtes is even
    if number % 2 == 0:
        # increment count if even
        even_count += 1

# print count of even
print(f"The number of even numbers are {even_count}")