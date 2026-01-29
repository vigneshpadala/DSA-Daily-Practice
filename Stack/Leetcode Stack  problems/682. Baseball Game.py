# 682. Baseball Game

class Solution(object):
    def calPoints(self, ops):
        stack=[]
        for ch in ops:
            if ch=="+":
                stack.append(stack[-1]+stack[-2])
            elif ch=="D":
                stack.append(2*stack[-1])
            elif ch=="C":
                stack.pop()
            else:
                stack.append(int(ch))

        return sum(stack)
