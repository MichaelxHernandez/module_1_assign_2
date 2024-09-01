# Michael Hernandez
# MMIS 6391
# Assignment 2.3
# 9/1/2024

# check if inventory restock is needed
def check_restock_inventory(inventory_level, reorder_level):
    return inventory_level < reorder_level

# calculate the reorder quantity
def calculate_reorder_quantity(inventory_level, reorder_level):
    return reorder_level - inventory_level

# main function
def main():
    # get the inventory level and reorder level from the user
    inventory_level = int(input("Enter the current inventory level: "))
    reorder_level = int(input("Enter the reorder level: "))

    # check if inventory restock is needed
    restock_needed = check_restock_inventory(inventory_level, reorder_level)
    if restock_needed:
        print("Restock Needed")
        reorder_quantity = calculate_reorder_quantity(inventory_level, reorder_level)
        print(f"Reorder Quantity: {reorder_quantity}")
    else:
        print("Restock Not Needed")

# call the main function
main()