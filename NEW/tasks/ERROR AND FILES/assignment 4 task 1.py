try:
    with open('sample.txt','r') as file:
        x=file.read()
        print(x)
except FileNotFoundError:
    print('Error: the file `sample.txt` was not found')