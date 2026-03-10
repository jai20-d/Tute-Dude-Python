#write a python program to print the Fibonacci series
n = int(input("Enter the number of terms you want in the Fibonacci series: "))
a = 0
b = 1 
count = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b
print()
print("Name : Jai Tomar")
print("Roll no: 2025UEA6527")