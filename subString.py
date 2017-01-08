def subs(a):
    """
    Generates a list of substrings
    """
    x = len(a)
    ls = []

    for i in range(x): # 0 - 3
        ls.append(a[i:]) # 0 hf
        j = len(a[i:])# 2
        for k in range(j): # 0 - 2
            ls.append(a[i:j]) # 0 - 2
            j -= 1 # 2-1=1
    return ls

print subs('1234')
