def m():
    s = str(input())
    if s[0] != "A":
        return "WA"
    if s[2:len(s)-3].count("C") != 1:
        return "WA"
    for c in s[1:]:
        if c == "C":
            continue
        if c.isupper():
            return "WA"
    return "AC"


print(m())
