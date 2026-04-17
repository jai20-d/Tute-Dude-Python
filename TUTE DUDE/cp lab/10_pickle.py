# 10. Store and read Python object using pickle
import pickle
data = {"name":"Jai","marks":90}
f = open("data.pkl","wb")
pickle.dump(data,f)
f.close()
f = open("data.pkl","rb")
print(pickle.load(f))
f.close()
print("Name: Jai Tomar Roll No.: 2025UEA6527")
