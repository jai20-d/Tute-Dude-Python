file2 = open('new.txt', 'w')
writing_file = file2.write('hello world')
print(writing_file)
file2.close()

file2 = open('new.txt', 'r')
print(file2.read())
file2.close()