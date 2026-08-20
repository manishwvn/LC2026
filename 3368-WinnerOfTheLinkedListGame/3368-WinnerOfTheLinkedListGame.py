# Last updated: 8/20/2026, 1:54:29 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        
        evens, odds = 0, 0

        curr = head

        while curr:
            if curr.val > curr.next.val:
                evens += 1
            else:
                odds += 1
            curr = curr.next.next

        if evens > odds:
            return "Even"
        elif odds > evens:
            return "Odd"
        else:
            return "Tie"
        