
s = "[([]])"
list_parenthese = []

for item in s:
    if item == "(" or item == "[" or item == "{":
        list_parenthese.append(item)
    elif item == ")":
        if len(list_parenthese) > 0 and '(' == list_parenthese[-1]:
            del list_parenthese[-1]
        else:
            print(False)
    elif item == "}":
        if len(list_parenthese) > 0 and '{' == list_parenthese[-1]:
            del list_parenthese[-1]
        else:
            print(False)
    elif item == "]":
        if len(list_parenthese) > 0 and '[' == list_parenthese[-1]:
            del list_parenthese[-1]
        else:
            print(False)
    else:
        pass
if len(list_parenthese) > 0:
    print(False)

# # list = ["[", "(", "["]
# list = [1, 2, 1]
# print(list[-1])
# list.remove(list[-1])
# print(list)