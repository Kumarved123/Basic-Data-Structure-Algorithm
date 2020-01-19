def postfixtoinfix(string):
    s = ['+','-','^','*','/']
    l = len(string)
    stack = []
    for i in string:
        if i not in s:
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append('('+b+i+a+')')
    return stack.pop()
print(postfixtoinfix('abc++'))