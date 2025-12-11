file2 = open('new.txt', 'a')
writing_file = file2.write(' \n may gawd bless us!')
print(writing_file)
file2.close()

file2 = open('new.txt', 'r')
print(file2.read())
file2.close()