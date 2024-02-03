import random


# Function to generate random marks for 5 students for 6 subjects
def generate_random_marks():
    marks = []
    for _ in range(4):
        student_marks = [random.randint(0, 100) for _ in range(6)]
        marks.append(student_marks)
    return marks


# Function to calculate average marks for each subject
def calculate_average_marks(marks):
    num_students = len(marks)
    num_subjects = len(marks[0])
    average_marks = [0] * num_subjects

    for i in range(num_subjects):
        subject_total = sum(marks[j][i] for j in range(num_students))
        average_marks[i] = subject_total / num_students

    return average_marks


# Function to determine the topper student
def find_topper_student(marks):
    average_marks = calculate_average_marks(marks)
    topper_index = average_marks.index(max(average_marks))
    return topper_index + 1  # Adding 1 to convert index to student number (1-based indexing)


# Generate random marks for 5 students
student_marks = generate_random_marks()

# Calculate average marks for each subject
average_marks = calculate_average_marks(student_marks)

# Determine the topper student
topper_student = find_topper_student(student_marks)

# Print average marks for each subject and the topper student
print("Average marks for each subject:", average_marks)
print("Topper student:", topper_student)
