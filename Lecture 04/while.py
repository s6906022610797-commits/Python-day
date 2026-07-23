keep_going = 'y'

while keep_going.upper() == 'Y':
    sales = float(input("Enter the amout of sales: "))
    comm_rate = float(input("Enter the commission rate (as a decimal): "))
    commission = sales * comm_rate
    print(f"The commission is ${commission:.2f}")
    
    keep_going = input("Do you want to calculate another sales amount? (y/n): ")