import random

import matplotlib.pyplot as plt

def display_marks_graph(marks):
    subjects = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5']
    plt.bar(subjects, marks, color='skyblue')
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title('Marks of a Student for a Subject')
    plt.xticks(subjects)
    plt.show()

# Example usage
marks = [random.randint(0,100)for _ in range(5)]
print(marks)
display_marks_graph(marks)
