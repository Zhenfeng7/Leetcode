import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        remain = nums[k:]
        heapq.heapify(heap)
        for i in remain:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        return heap[0]