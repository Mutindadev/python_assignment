first_number = input("enter the first number")
second_number = input("enter the second number")
#sum_of_numbers = int(first_number) + int(second_number)
#print("The sum of the two numbers is:", sum_of_numbers)
#print("Thank you for using the sum calculator!")

subtract_number = input("enter the number to subtract from the first number")
first_number = int(first_number)
second_number = int(second_number)
subtract_number = int(subtract_number)
result = first_number - subtract_number
print("The result of subtracting", subtract_number, "from", first_number, "is:", result)
number = input("Enter a number to check if it is even or odd: ")
if number.isdigit():
    number = int(number)
    if number % 2 == 0:
        print(number, "is an even number.")
    else:
        print(number, "is an odd number.")
else:
    print("Please enter a valid integer.")
# The code above performs subtraction and checks if a number is even or odd.
# It prompts the user for two numbers, subtracts a third number from the first,
# and checks if a given number is even or odd, providing appropriate messages.
# The code above performs subtraction and checks if a number is even or odd.