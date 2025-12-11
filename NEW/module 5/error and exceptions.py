try:
    a=2
    b=0
    print(a/b)
except ZeroDivisionError:
    print('error in Division by zero')
finally:
    print('try again')