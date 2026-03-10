#write a python program to make such pattern like a right angled triangle with a number increase by 1
n = int(input("Enter the number of rows: "))
t=1
for i in range(n):
    for j in range(i+1):
        print(t, end = " ")
        t=t+1
    print()
print("Name : Jai Tomar")
print("Roll no: 2025UEA6527")