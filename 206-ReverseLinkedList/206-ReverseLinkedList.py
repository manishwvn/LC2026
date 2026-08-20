# Last updated: 8/20/2026, 2:15:53 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        curr_node, prev_node, next_node = head, None, head.next

        while curr_node.next is not None:
            
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next

        curr_node.next = prev_node

        return curr_node

        