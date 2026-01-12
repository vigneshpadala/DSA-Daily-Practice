# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev=None
        temp=head
        while temp:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        return prev
