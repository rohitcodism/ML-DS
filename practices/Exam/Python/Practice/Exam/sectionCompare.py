import matplotlib.pyplot as plt
import numpy as np
import random

def generate_random_marks(num_sections, num_students_per_section):
    # Generate random marks for each section
    marks = [[random.randint(0, 100) for _ in range(num_students_per_section)] for _ in range(num_sections)]
    print(marks)
    return marks

def calculate_average_marks(marks):
    # Calculate the average marks (CGPA) for each section
    averages = [np.mean(section_marks) for section_marks in marks]
    print(averages)
    return averages

def plot_average_marks(averages):
    # Plot the average marks for each section
    sections = [f"Section {i+1}" for i in range(len(averages))]
    plt.bar(sections, averages, color='skyblue')
    plt.xlabel('Sections')
    plt.ylabel('Average Marks (CGPA)')
    plt.title('Average Marks (CGPA) of 10 Sections')
    plt.xticks(rotation=45)
    plt.show()

# Generate random marks for 10 sections with 20 students each
num_sections = 10
num_students_per_section = 20
section_marks = generate_random_marks(num_sections, num_students_per_section)

# Calculate the average marks (CGPA) for each section
averages = calculate_average_marks(section_marks)

# Plot the average marks for each section
plot_average_marks(averages)
