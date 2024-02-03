def simple_interest(principal, rate, time):
    # Simple Interest = (Principal * Rate * Time) / 100
    interest = (principal * rate * time) / 100
    amount = principal + interest
    return amount

def compound_interest(principal, rate, time):
    # Compound Interest = Principal * ((1 + Rate/100) ** Time)
    amount = principal * ((1 + rate/100) ** time)
    return amount

# Example usage
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percent): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest_amount = simple_interest(principal, rate, time)

# Calculate compound interest
compound_interest_amount = compound_interest(principal, rate, time)

print("\nAmount payable after simple interest: {:.2f}".format(simple_interest_amount))
print("Amount payable after compound interest: {:.2f}".format(compound_interest_amount))
