# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Get the count of nodes
        count = 0
        c = head
        while c:
            count += 1
            c = c.next
        avg = count // k
        extra = count % k
        
        ans = []
        cur = head
        for i in range(k):
            h = cur
            for j in range(avg +  (extra > i) - 1):
                if cur: cur = cur.next
                    
            if cur: cur.next, cur = None, cur.next
            ans.append(h)
        return ans
            