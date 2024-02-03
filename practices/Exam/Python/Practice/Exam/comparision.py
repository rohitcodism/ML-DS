import matplotlib.pyplot as plt
import numpy as np
import random

def generate_random_marks():
    # Generate random marks for 6 unit tests for two students
    student1_marks = [random.randint(0, 100) for _ in range(6)]
    student2_marks = [random.randint(0, 100) for _ in range(6)]
    return student1_marks, student2_marks

def compare_marks(student1_marks, student2_marks):
    # Create a bar graph to compare the marks of the two students
    labels = ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5', 'Test 6']
    x = np.arange(len(labels))
    width = 0.35
    print(x)

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, student1_marks, width, label='Student 1')
    rects2 = ax.bar(x + width/2, student2_marks, width, label='Student 2')

    ax.set_xlabel('Unit Test')
    ax.set_ylabel('Marks')
    ax.set_title('Comparison of Marks for Two Students')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()

# Generate random marks for two students
student1_marks, student2_marks = generate_random_marks()

# Compare the marks using a bar graph
compare_marks(student1_marks, student2_marks)
