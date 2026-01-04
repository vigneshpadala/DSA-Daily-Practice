#Find Length of String (Without len() Function)

def s_length(s):
    count=0
    for i in range(0,len(s)):
        count+=1
    return count

s="vigneshpatel"
print(s_length(s))
