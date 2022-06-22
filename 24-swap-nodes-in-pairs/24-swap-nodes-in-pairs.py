# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        prev, cur, ans = None, head, head.next
        while cur and cur.next:
            temp = cur.next
            if prev: prev.next = temp
                
            cur.next, temp.next = temp.next, cur
            prev, cur = cur, cur.next
        return ans
            