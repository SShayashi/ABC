
def m():
    s = str(input())
    i = s.index("WW")
    if s[i+5:i+7] == "WW":
        d = {
            0: "Si",
            1: "La",
            2: "La",
            3: "So",
            4: "So",
            5: "Fa",
            6: "Fa",
            7: "Mi",
            8: "Re",
            9: "Re",
            10: "Do",
            11: "Do",
        }
    else:
        d = {
            0: "Mi",
            1: "Re",
            2: "Re",
            3: "Do",
            4: "Do",
            5: "Si",
            6: "La",
            7: "La",
            8: "So",
            9: "So",
            10: "Fa",
            11: "Fa",
        }
    return d.get(i)

print(m())