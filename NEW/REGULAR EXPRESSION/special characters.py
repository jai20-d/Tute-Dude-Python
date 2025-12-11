import re
s1 = "PYthon is a programming language"

#[A-Z][a-z]

pat= r"[A-z][A-z][a-z]"
match_obj=re.search(pat,s1)
print(match_obj)
