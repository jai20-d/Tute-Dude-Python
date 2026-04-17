# 20. Create a program to generate square, cube and factorial values in a dictionary
import math
d = {}
for i in range(1,6):
    d[i] = (i*i, i*i*i, math.factorial(i))
print(d)
print("Name: Jai Tomar Roll No.: 2025UEA6527")
