# 6. Create a program to store student marks and assign grades using NumPy
import numpy as np
marks = np.array([85,72,90,60,50])
grades = []
for m in marks:
    if m>=80: grades.append('A')
    elif m>=60: grades.append('B')
    else: grades.append('C')
print("Marks:", marks)
print("Grades:", grades)
print("Name: Jai Tomar Roll No.: 2025UEA6527")
