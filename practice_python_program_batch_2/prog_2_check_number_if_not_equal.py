# ask user to input two numbers
input_number_one = int(input("Input First Number:"))
input_number_two = int(input("Input Second Number:"))

# check if the inputted numbers are not the same
if input_number_one != input_number_two:
    # if not same, print "Not Equal"
    print("Not Equal")
else:
    # if same, print "Equal"
    print("Equal")