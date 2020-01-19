def parenthesis(A):
    stack = []
    open = ('(', '{','[')
    close = ('}',']',')')
    for i in A:
        if i in open:
            stack.append(i)
        if i in close:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if i == ')':
                if top != '(':
                    return False
            elif i == '}':
                if top != '{':
                    return False
            elif i ==']':
                if top != '[':
                    return False
    if len(stack) != 0:
        return False
    return True

expr = "((alf)ls)"
print(parenthesis(expr))


