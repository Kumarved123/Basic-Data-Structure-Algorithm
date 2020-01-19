def peek(stack):
    return stack[-1]
def isOperand(c):
    s = ('+', '-', '*', '/')
    if c not in s:
        return True
    return False
def isLeftParenthesis(c):
    s = ('(','{','[')
    if c in s:
        return True
    return False
def isRightParenthesis(c):
    s = ('}',')',']')
    if c in s:
        return True
    return False
def isEmpty(s):
    if len(s) == 0:
        return True
    return False
def hasLessOrEqualPriority(a, b):
    priority = [['-','+'], ['*','/'] ,['^'], ['}',')',']','(','{','[']]
    for i in range(4):
        if a in priority[i]:
            a = i
        if b in priority[i]:
            b = i
    if a<b:
        return True
    else:
        return False

def toPostfix(infix):
    stack = []
    postfix = ''

    for c in infix:
        if isOperand(c):
            postfix += c
        else:
            if isLeftParenthesis(c):
                stack.append(c)
            elif isRightParenthesis(c):
                operator = stack.pop()
                while not isLeftParenthesis(operator):
                    postfix += operator
                    operator = stack.pop()
            else:
                while (not isEmpty(stack)) and hasLessOrEqualPriority(c,peek(stack)):
                    postfix += stack.pop()
                stack.append(c)

    while (not isEmpty(stack)):
        postfix += stack.pop()
    return postfix