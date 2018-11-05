def abbreviate(s):
    res = ""
    now = ""
    for c in s + " ":
        if c.isalpha():
            now += c
        else:
            if len(now) > 3:
                res += now[0] + str(len(now) - 2) + now[-1] + c
            elif len(now) >= 1:
                res += now + c
            else:
                res += c
            now = ""
    return res[:-1]


print(abbreviate('about.you'))