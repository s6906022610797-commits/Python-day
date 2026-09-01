num_days = int(input('For how many days do you want to enter sales? '))
with open('sales.txt', 'w') as sales_file:
    for day in range(1, num_days + 1):
        sales = float(input(f'Enter the sales for day {count}: '))
        sales_file.write(str(sales) + '\n')

print('Data written to sales.txt')