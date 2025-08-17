# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount only if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return original price if discount < 20%


# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call function
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {final_price:.2f}")