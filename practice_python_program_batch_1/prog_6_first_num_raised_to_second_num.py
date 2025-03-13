# ask user to input two numbers
input_number_one = int(input("Input First Number: "))
input_number_two = int(input("Input Second Number: "))

# check if input is zero and exponent is negative
if input_number_one == 0 and input_number_two < 0:
    print("0 cannot be raised to a negative power.")
else:
    # raise the first number to the power of second number
    result = input_number_one ** input_number_two

    # print result
    print(result)