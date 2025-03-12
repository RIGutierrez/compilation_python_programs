# ask user to input two numbers
input_number_one = int(input("Input First Number:"))
input_number_two = int(input("Input Second Number:"))

# check if input 1 is smaller compared to input 2
if input_number_one > input_number_two:

    # swap values to make input one smaller
    input_number_one, input_number_two = input_number_two, input_number_one

# loop to print numbers between two numbers
for number in range(input_number_one + 1, input_number_two):
    # print number
    print(number)

