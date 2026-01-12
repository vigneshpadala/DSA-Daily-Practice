# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        count = 0
        itr = head

        
        while itr:
            count += 1
            itr = itr.next

        
        mid = count // 2

        itr = head
        for i in range(mid):
            itr = itr.next

       
        return itr
