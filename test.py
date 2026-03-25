# import re

# _text = "([)]"

# for x in range(int(len(_text)/2)):    
#     match = re.search(r"\(\)|\{\}|\[\]", _text)
#     if match:
#         _text = _text[:match.start()] + _text[match.end():]     

  
# if _text == "" :
#        print(True)
# else :
#       print(False)




s ="([)]"
pairs = {
')': '(',
']': '[',
'}': '{'
}

stack = []

for char in s:
    if char in pairs:  # closing bracket
        if not stack or stack[-1] != pairs[char]:
             print(False)
        stack.pop()
    else:
        stack.append(char)  
print(len(stack) == 0)