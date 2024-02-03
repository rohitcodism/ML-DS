import random

def generate_random_marks():
    # Generate random marks for 5 students for 6 subjects
    marks = [[random.randint(0, 100) for _ in range(6)] for _ in range(5)]
    return marks

def increment_marks(marks, increment_value=5):
    # Increment each mark by the specified value (default is 5)
    for i in range(len(marks)):
        for j in range(len(marks[i])):
            marks[i][j] += increment_value
    return marks

# Generate random marks for 5 students for 6 subjects
student_marks = generate_random_marks()

# Increment each mark by 5
final_marks = increment_marks(student_marks)

# Print the final marks
print("Final Marks:")
for i, marks in enumerate(final_marks, 1):
    print("Student", i, ":", marks)
