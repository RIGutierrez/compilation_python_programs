# list to store value
numbers = []

while True:
    try:
        # ask user to input numbers
        number = int(input("Please input a number: "))

        # store number in numbers
        numbers.append(number)
    
    # break if invalid
    except ValueError:
        print("Invalid input")
        break

# check highest number   
if numbers: 
    print(f"The highest number inputted is: {max(numbers)}")
else:
    print("No value inputted")