# ask user to input two numbers
input_number_one = int(input("Input First Number:"))
input_number_two = int(input("Input Second Number:"))

# check if inputted second number is not 0
if input_number_two == 0:
    print("Dividing a number by 0 is not allowed.")

# if not 0, proceed
else:
    quotient_remainder = input_number_one % input_number_two

    #print remainder
    print(quotient_remainder)

    


