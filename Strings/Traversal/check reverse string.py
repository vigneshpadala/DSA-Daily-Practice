def reverse_str(s):
    new_s=""
    for char in s:
        for l in char:
            if l.isalnum():
                new_s+=l.lower()
    
    new_u=""
    for i in s:
        new_u=i+new_u
        
    if new_s==new_u:
        return True
    else:
        return False
    
    
s="viggi, patel:, Padala"
print(reverse_str(s))
