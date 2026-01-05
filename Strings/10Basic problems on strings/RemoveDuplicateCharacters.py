#Remove Duplicate Characters

def removes_duplicates(s):
    res=""
    for ch in s:
        if ch not in res:
            res+=ch

    return res


s="viggi"
print(removes_duplicates(s))
