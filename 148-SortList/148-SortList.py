# Last updated: 8/20/2026, 2:16:54 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def find_mid(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def merge(self, left, right):
        tail = dummy = ListNode()

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next

            else:
                tail.next = right
                right = right.next

            tail = tail.next

        if left:
            tail.next = left

        if right:
            tail.next = right

        return dummy.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not head or not head.next: return head
        
        #split
        left = head
        right = self.find_mid(head)
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
    
    
        
        