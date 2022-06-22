# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for i in range(n - 1):
            fast = fast.next
        if fast.next is None:
            head = head.next
            return head
        
        while fast.next.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        