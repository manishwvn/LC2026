# Last updated: 8/20/2026, 2:18:27 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        node = head
        
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
                
            else:
                node = node.next
                
        return head
            