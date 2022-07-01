class Solution:
    def maxArea(self, height: List[int]) -> int:
        lef, rig = 0, len(height) - 1
        imax = 0
        while lef < rig:
            imax = max(imax, (rig - lef) * min(height[lef], height[rig]))
            if height[lef] > height[rig]:
                rig -= 1
            else: lef += 1
        return imax