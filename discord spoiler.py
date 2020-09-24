import pyperclip
string = input("input a string\n")
result = ""
for i in string:
    result += "||"+i+"||"
print(result)
pyperclip.copy(result)