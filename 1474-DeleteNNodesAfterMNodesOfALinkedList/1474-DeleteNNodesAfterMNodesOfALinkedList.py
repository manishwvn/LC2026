# Last updated: 10/7/2026, 2:56:33 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:

        curr = head
        last = None

        while curr:
            m_count, n_count = m, n

            while curr and m_count:
                last = curr
                curr = curr.next
                m_count -= 1

            while curr and n_count:
                curr = curr.next
                n_count -= 1

            last.next = curr
        
        return head

