class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        ans = 1
        usedChar = {s[0]: 0}
        i = 0 
        j = 1
        while j < len(s):
            if s[j] in usedChar and usedChar[s[j]] >= i:
                ans = max(ans, j - i)
                i = usedChar[s[j]] + 1
                usedChar[s[j]] = j
                
                j += 1
                
            else:
                usedChar[s[j]] = j
                j += 1
                
        return max(j - i, ans)