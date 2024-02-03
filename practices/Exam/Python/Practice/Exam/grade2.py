def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        return 'O'
    elif marks >= 80 and marks < 90:
        return 'E'
    elif marks >= 70 and marks < 80:
        return 'A'
    elif marks >= 60 and marks < 70:
        return 'B'
    elif marks >= 50 and marks < 60:
        return 'C'
    elif marks >= 40 and marks < 50:
        return 'D'
    elif marks >= 0 and marks < 40:
        return 'F (FAILED)'
    else:
        return 'INVALID'

# Example usage
marks = float(input("Enter the marks obtained by the student: "))
grade = calculate_grade(marks)
print("Grade:", grade)
