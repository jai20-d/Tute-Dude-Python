file = open('new.txt', 'r+')
x=file.write('welcome')
print(x)
file.close()

file = open('new.txt', 'r+')
y=file.read()
print(y)
file.close()
print()

'''''' #OR

with open('new.txt','w') as file:
    x=file.write('aur byii')
    print(x)

with open('new.txt','r') as file:
    y=file.read()
    print(y)