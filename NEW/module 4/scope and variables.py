n=1 #global variable (can be in both in and out of function)

def fn():
    #use global cmd
    n =5 #local variable (only in function)
    print('in',n)

fn()

print('out',n)