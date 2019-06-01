

def m():
    n = int(input())
    s = str(input())
    exleft = 0
    exright = 0
    for c in s:
        if c == "(":
            exleft +=1

        elif c == ")":
            if exleft <= 0:
                exright +=1
            else:
                exleft -=1
    return "(" * exright + s + ")" * exleft

print(m())