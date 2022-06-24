# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        ans_stack = []
        cur1, cur2 = l1, l2
        while cur1 or cur2:
            if cur1:
                stack1.append(cur1.val)
                cur1 = cur1.next
            if cur2:
                stack2.append(cur2.val)
                cur2 = cur2.next
        carry = 0
        while stack1 or stack2 or carry:
            val = 0
            if stack1: val += stack1.pop()
            if stack2: val += stack2.pop()
            val += carry
            carry = val // 10
            val = val % 10
            ans_stack.append(val)
        
        res = ListNode()
        cur = res
        while ans_stack:
            cur.next = ListNode(ans_stack.pop())
            cur = cur.next
        return res.next


        
