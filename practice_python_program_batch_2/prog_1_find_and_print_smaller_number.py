# ask user to input two numbers
input_number_one = int(input("Input First Number: "))
input_number_two = int(input("Input Second Number: ")) 

# compare inputted two numbers
if input_number_one < input_number_two:
    # print the smaller number
    print(f"The smaller number is: {input_number_one}")
elif input_number_one > input_number_two:
    print(f"The smaller number is: {input_number_two}")
else:
    print("Both numbers are equal.")