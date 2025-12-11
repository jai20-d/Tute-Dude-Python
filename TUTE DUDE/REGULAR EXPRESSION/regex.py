import re


message= "the current version of python is 5.43. others are 5.11 5.46 5.87 "
"""
print("python" in message)
print(message.find("python"))
print(message.find("7"))

"""
match_obj = re.search("5.46", message)
print(match_obj)
print()

if match_obj :
    print("found")
else:
    print("not found")

print(message[55:59])