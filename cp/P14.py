#write a python program to find the repeated item in the tuple
tup1 = (1, 2, 3, 4, 5, 3, 5, 4)
repeated = []
for item in tup1:
    if tup1.count(item)>1:
        if item not in repeated:
            repeated.append(item)
print("The repeated items are: ", repeated)
print("Name : Jai Tomar")
print("Roll no: 2025UEA6527")