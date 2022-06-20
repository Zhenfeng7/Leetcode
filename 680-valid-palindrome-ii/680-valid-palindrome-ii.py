class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self._isPanlindrome(s, left, right - 1) or self._isPanlindrome(s, left + 1, right)
            left, right = left + 1, right - 1
        return True
    
    
    
    def _isPanlindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True