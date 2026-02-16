# leetcode problem 74
# search Matrix element they  or not

class Solution(object):
    def (self, matrix, target):
        for row in matrix:
            for col in row:
                if target == col:
                    return True
        return False

# using binary search

class Solution(object):
    def searchMatrix(self, matrix, target):
        rows=len(matrix)
        cols=len(matrix[0])

        l=0
        h=(rows*cols)-1

        while l<=h:
            mid = (l+h)//2
            row=mid//cols
            col=mid%cols
            middle_value=matrix[row][col]

            if middle_value==target:
                return True
            elif middle_value<target:
                l=mid+1
            else:
                h=mid-1
        return False
