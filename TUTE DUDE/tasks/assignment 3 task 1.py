n=input('enter number: ')
n=int(n)
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)  #4*3!
result = factorial(n)
print(f'Factorial of {n} is' ,result)
