# 1876. Substrings of Size Three with Distinct Characters

# o(n3)
class Solution(object):
    def countGoodSubstrings(self, s):
        ans=0
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                temp=[]
                for k in range(i,j+1):
                    temp.append(s[k])
                if len(temp)==3 and len(set(temp))==3:
                    ans+=1
        return ans

  # o(n) 
