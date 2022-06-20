#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        carry = 0
        cur = result
        while l1 or l2 or carry:
            sum = 0 
            if l1: sum += l1.val
            if l2: sum += l2.val
            sum += carry
            carry = sum // 10
            sum = sum % 10
            cur.next = ListNode(sum)
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            cur = cur.next
        return result.next
        