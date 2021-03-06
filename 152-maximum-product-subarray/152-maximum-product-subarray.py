class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax, imin, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            candidates = (nums[i], imax * nums[i], imin * nums[i])
            imax = max(candidates)
            imin = min(candidates)
            ans = max(ans, imax)
        return ans