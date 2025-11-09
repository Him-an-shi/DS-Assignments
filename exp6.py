'''6	In any language program,  mostly syntax errors occur due to unbalancing delimiter such as (),{},[].
 Write a program using stack to check whether given expression is well parenthesized or not using stack 
 (Implement Stack class/ don’t use in built stack library) '''
# Custom Stack Class
class Stack:
    def __init__(self):
        self.items = []  # Internal list to store stack elements

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Function to check for balanced parentheses
def is_balanced(expression):
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    matching = {")": "(", "]": "[", "}": "{"}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != matching[char]:
                return False  # Mismatch or stack empty
    
    return stack.is_empty()  # True if no unmatched opening left


# Driver Code
expr = input("Enter an expression to check: ")

if is_balanced(expr):
    print("The expression is well parenthesized (Balanced). ✅")
else:
    print("The expression is not well parenthesized (Unbalanced). ❌")
