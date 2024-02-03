def get_status(age):
    if age < 2:
        return "in born"
    elif age <= 10:
        return "child"
    elif age <= 17:
        return "young"
    elif age <= 49:
        return "adult"
    elif age <= 79:
        return "old"
    else:
        return "very old"

# Example usage
ages = [1, 5, 12, 25, 55, 85]

for age in ages:
    status = get_status(age)
    print(f"Age {age}:", status)
