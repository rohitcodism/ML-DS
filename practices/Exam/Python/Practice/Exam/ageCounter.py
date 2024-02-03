def count_age_groups(ages):
    age_groups = {'26-35': 0, '36-45': 0, '46-55': 0}
    for age in ages:
        if 26 <= age <= 35:
            age_groups['26-35'] += 1
        elif 36 <= age <= 45:
            age_groups['36-45'] += 1
        elif 46 <= age <= 55:
            age_groups['46-55'] += 1
    return age_groups

# Input number of employees
n = int(input("Enter the number of employees: "))

# Input ages of employees
ages = []
for i in range(n):
    age = int(input(f"Enter age of employee {i+1}: "))
    ages.append(age)

# Count the number of persons in each age group
age_group_counts = count_age_groups(ages)

# Print the counts
print("\nAge group counts:")
for age_group, count in age_group_counts.items():
    print(f"{age_group}: {count}")