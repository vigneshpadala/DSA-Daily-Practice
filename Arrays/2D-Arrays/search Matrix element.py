# search Matrix element they  or not

class Solution(object):
    def (self, matrix, target):
        for row in matrix:
            for col in row:
                if target == col:
                    return True
        return False
