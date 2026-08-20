# Last updated: 8/20/2026, 2:09:32 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        length, curr = 0, head

        while curr:
            length += 1
            curr = curr.next
        
        base, extra = length // k, length % k
        curr, result = head, []

        for i in range(k):
            part_head = curr
            part_size = base + 1 if extra > 0 else base
            if extra > 0:
                extra -= 1

            for j in range(part_size - 1):
                if curr:
                    curr = curr.next

            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

            result.append(part_head)

        return result
            
        