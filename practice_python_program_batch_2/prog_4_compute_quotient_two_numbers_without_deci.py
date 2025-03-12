# ask user to input two numbers
input_number_one = int(input("Input First Number:"))
input_number_two = int(input("Input Second Number:"))

# check if second number is 0
if input_number_two == 0:
    # 0 is not allowed
    print("Dividing a number by 0 is not allowed.")

else:
    # calculate the quotient of inputted two numbers (w/o decimal)
    quotient_without_decimal = input_number_one // input_number_two
    print(quotient_without_decimal)   