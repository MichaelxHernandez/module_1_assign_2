# Michael Hernandez
# MMIS 6391
# Assignment 2.1
# 9/1/2024


# calculate the sales tax for a given amount
def calculate_sales_tax(amount, tax_rate):
    return amount * tax_rate

# calculate the total amount after sales tax
def calculate_total_amount(amount, tax_rate):
    return amount + calculate_sales_tax(amount, tax_rate)

# main function
def main():
    # get the amount and tax rate from the user
    amount = float(input("Enter the purchase amount: "))
    tax_rate = float(input("Enter the sales tax rate (as a decimal): "))

    # calculate the sales tax
    sales_tax = calculate_sales_tax(amount, tax_rate)
    print(f"Sales Tax: ${sales_tax:.2f}")

    # calculate the total amount
    total_amount = calculate_total_amount(amount, tax_rate)
    print(f"Total Amount: ${total_amount:.2f}")

# call the main function
main()
