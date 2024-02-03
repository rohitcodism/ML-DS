def calculate_bill(units):
    if units <= 200:
        return units * 0.50
    elif 201 <= units <= 400:
        return 100 + (units - 200) * 0.65
    elif 401 <= units <= 600:
        return 250 + (units - 400) * 0.80
    else:
        return 425 + (units - 600) * 1.25

# Example usage
units_consumed = float(input("Enter the number of units consumed: "))
bill_amount = calculate_bill(units_consumed)
print("Amount to be paid by the consumer: Rs.", bill_amount)
