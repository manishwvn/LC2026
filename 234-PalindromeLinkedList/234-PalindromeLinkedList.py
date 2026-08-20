# Last updated: 8/20/2026, 2:15:13 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def find_mid(node):
            slow, fast = node, node

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def reverse_list(node):
            prev, curr, nxt = None, node, node.next

            while nxt:
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = nxt.next

            curr.next = prev
            return curr

        mid_node = find_mid(head)
        head_2 = reverse_list(mid_node)

        while head and head_2:
            if head.val != head_2.val:
                return False
            
            head = head.next
            head_2 = head_2.next
        
        return True
        