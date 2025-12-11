import re

message= "the current version of python is 5.43. others are 5.11 5.46 5.87 "

match_object = re.search("[0-9][0-9]", message)
print(match_object)

match_object = re.search("[0-9][0-9]", "house number 251-A 25/64")
print(match_object)

match_object = re.search("[0-9][0-9][0-9]", "house number 251-A 25/64")
print(match_object)

match_object = re.search("[0-9].[0-9][0-9]", message)
print(match_object)
