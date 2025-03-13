# list to store values
numbers = []
count = 0
total_sum = 0

while True:
    try:
        # ask user to input numbers
        number = int(input("Please input a number: "))
        
        # increment count for total sum
        total_sum += number
        count += 1

    # break if invalid
    except ValueError:
        break

# display average
if count > 0:
    average = total_sum / count 
    print(f"The average of the inputted numbers is: {average:.2f}")
else:
    print("No value inputted")