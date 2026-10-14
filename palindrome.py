def palin(s):
    if len(s)<=1:
        return "palindrome"
    else:
        if s[0]==s[-1]:
            palin(s[0:-1])
            return "palin"
        else:
            return "not palin"
print(palin('madam'))
print(palin('malyalam'))
print(palin('raj'))
print(palin('abccba'))
