class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = [nums[0]]
        maxi = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i] if localMax[i - 1] <= 0 else nums[i] + localMax[i - 1]
            localMax.append(cur)
            maxi = max(maxi, localMax[i])
        return maxi