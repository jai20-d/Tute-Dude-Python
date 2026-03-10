#create a dict of a number and compute square cubic factorial
def cube(n):
    return n**3
def square(n):
    return n**2
def fact(n):
    t=1
    for i in range(1, n+1):
        t=t*i
    return t
numbers = [1, 2, 3, 4, 5]
dict1= {x: {"square": square(x),
            "cube": cube(x),
            "factorial": fact(x)
            }
            for x in numbers}
print(dict1)
print("Name : Jai Tomar")
print("Roll no: 2025UEA6527")