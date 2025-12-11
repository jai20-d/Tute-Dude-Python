#1
#directory
#mode- read(r) write(w) append(a) read+write(r+)
file1= open('hey.txt' ,'r')
read_file = file1.read() #put number in bracket to get those many characters
print(read_file)
file1.close()
print()
''''''
#2
with open('hey.txt','r') as file1:
    read_file = file1.read()  # put number in bracket to get those many characters
    print(read_file)