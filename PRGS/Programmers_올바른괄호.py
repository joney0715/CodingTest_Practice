def solution(s):
    if s[0] == ')':
        return False
    
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')' and len(stack):
            stack.pop()
        else:
            return False

    if len(stack) != 0:    
        return False
    else:
        return True