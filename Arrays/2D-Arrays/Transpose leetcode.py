# Transpose leetcode - 867
class Solution(object):
    def transpose(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        result=[[0]* m for _ in range(n)]
        # [[0,0,0],[0,0,0],[0,0,0]]

        for i in range(n):
            result[j][i]=matrix[i][j]
        return result
