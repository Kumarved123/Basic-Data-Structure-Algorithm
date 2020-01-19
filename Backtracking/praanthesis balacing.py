def util(N, p , o, c):
    if c == N:
        print(''.join(p))
        return
    else:
        if o>c:
            p.append(')')
            util(N, p, o, c+1)
            p.pop()
        if o < N:
            p.append('(')
            util(N, p, o+1, c)
            p.pop()
    return

def paran(N):
    p = []
    o = 0
    c = 0
    util(N, p, o, c)

paran(3)