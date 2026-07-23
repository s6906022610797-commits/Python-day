hours = int(input("Enter the number of hours worked: "))
rate = float(input("Enter the number of pay rate: "))
if hours <= 40:
    total_pay = hours * rate
else:
    overtime_hours = hours - 40
    total_pay = (40 * rate) + (overtime_hours * rate * 1.5)
    
print("Total pay: ",total_pay)