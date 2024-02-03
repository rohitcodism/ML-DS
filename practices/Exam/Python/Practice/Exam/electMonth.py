def read_electricity_bills(filename):
    electricity_bills = {}
    with open(filename, 'r') as file:
        for line in file:
            customer_id, month, consumption = line.strip().split()
            if month not in electricity_bills:
                electricity_bills[month] = {}
            electricity_bills[month][customer_id] = float(consumption)
    print(electricity_bills.items())
    return electricity_bills

def print_monthly_consumption(electricity_bills, month):
    if month in electricity_bills:
        print(f"Electricity consumption for {month}:")
        for customer_id, consumption in electricity_bills[month].items():
            print(f"Customer ID: {customer_id}, Consumption: {consumption}")
    else:
        print(f"No data available for {month}")

# Read electricity bills from file
electricity_bills = read_electricity_bills(
    'current.txt')

# Print electricity consumption for July
print_monthly_consumption(electricity_bills, 'July')

# Print electricity consumption for November
print_monthly_consumption(electricity_bills, 'November')
