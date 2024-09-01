# Michael Hernandez
# MMIS 6391
# Assignment 2.2
# 9/1/2024

#calculate the overtime pay
def calculate_overtime_pay(hours_worked, hourly_rate):
    return (hours_worked - 40) * hourly_rate

#calculate the total pay
def calculate_total_pay(hours_worked, hourly_rate):
    if hours_worked > 40:
        return 40 * hourly_rate + calculate_overtime_pay(hours_worked, hourly_rate)
    else:
        return hours_worked

#main function
def main():
    #get the hours worked and hourly rate from the user
    hours_worked = float(input("Enter the hours worked: "))
    hourly_rate = float(input("Enter the hourly rate: "))

    #calculate the total pay
    total_pay = calculate_total_pay(hours_worked, hourly_rate)
    print(f"Total Pay: ${total_pay:.2f}")

#call the main function
main()
