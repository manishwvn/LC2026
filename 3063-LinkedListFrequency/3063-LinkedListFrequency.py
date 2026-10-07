# Last updated: 10/7/2026, 2:45:53 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hm = {}

        while head:
            if head.val in hm:
                hm[head.val] += 1
            else:
                hm[head.val] = 1
            
            head = head.next

        new_head = ListNode()
        curr = new_head

        for k, v in hm.items():
            curr.next = ListNode(v)
            curr = curr.next
        
        return new_head.next