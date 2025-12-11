file= open('output.txt','w')
write=file.write('hello, Python!')
file.close()

file= open('output.txt','a')
writing_file= file.write(' \nlearning file handling in python.Data succesfully appended.')
file.close()

file= open('output.txt','r')
reading_file= file.read()
print(reading_file)
file.close()
