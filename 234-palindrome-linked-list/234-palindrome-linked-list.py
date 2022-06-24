# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        
        # reverse the second half
        prev = None
        while slow:
            cur = slow
            slow = slow.next
            cur.next = prev
            prev = cur
        # slow became None, prev is the head of the second half list
        while prev:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next
        
        return True