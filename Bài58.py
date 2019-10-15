import re
s = input()
lst_email = []
lst_email = re.findall("(\w+)@(\w+).(\w+)",s)
print(lst_email)
print(lst_email[0])
