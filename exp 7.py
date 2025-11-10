'''7	Write a program for expression conversion from infix to postfix. '''
def precedence(char):
    if char  in ["*","/"]:
        return 2
    elif char in ["+","-"]:
        return 1
    else:
        return 0
stack=[]
result=""
exp=input("expression in infix form: ")
for char in exp:
    if char.isalnum():
        result+=char
    elif char=="(":
        stack.append(char)
    elif char==")":
        while stack and stack[-1]!="(":
            result+=stack.pop()
        stack.pop()
    else: 
        while stack and precedence(stack[-1])>=precedence(char):
            result+=stack.pop()
        stack.append(char)
while stack:
    result+=stack.pop()
print(f"postfix form {result}")