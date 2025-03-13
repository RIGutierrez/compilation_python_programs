# list to store value
numbers = []

while True:
    try:
        # ask user to input numbers
        number = int(input("Please input a number: "))
        
        # store number to numbers
        numbers.append(number)
    
    # break if invalid
    except ValueError:
        break

# sort numbers highest to lowest
if numbers:
    numbers.sort(reverse=True)
    print(f"Numbers from highest to lowest: {numbers}")
else:
    print("No value inputted")