class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i in range(len(nums) - 1):
            ans.append(nums[i] * ans[i])
        right = 1
        for j in range(len(nums) - 1, -1, -1):
            ans[j] *= right
            right *= nums[j]
        return ans