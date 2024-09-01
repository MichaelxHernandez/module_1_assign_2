# Michael Hernandez
# MMIS 6391
# Assignment 2.4
# 9/1/2024

# calculate the discount based on customer loyalty level
def calculate_discount(amount, loyalty_level):
    if loyalty_level == "gold":
        return amount * 0.10
    elif loyalty_level == "silver":
        return amount * 0.05
    else:
        return

# calculate the total amount after discount
def calculate_total_amount(amount, loyalty_level):
    discount = calculate_discount(amount, loyalty_level)
    if discount:
        return amount - discount
    else:
        return amount

# main function
def main():
    # get the amount and loyalty level from the user
    amount = float(input("Enter the purchase amount: "))
    loyalty_level = input("Enter the customer loyalty level (gold/silver): ")

    # calculate the discount
    discount = calculate_discount(amount, loyalty_level)
    if discount:
        print(f"Discount: ${discount:.2f}")

    # calculate the total amount
    total_amount = calculate_total_amount(amount, loyalty_level)
    print(f"Total Amount: ${total_amount:.2f}")

# call the main function
main()