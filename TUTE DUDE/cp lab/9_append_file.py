# 9. Append text to a file and display
f = open("sample.txt","a")
f.write("\ni am studying in ECAM 1!!")
f.close()
f = open("sample.txt","r")
print(f.read())
f.close()
print("Name: Jai Tomar Roll No.: 2025UEA6527")
