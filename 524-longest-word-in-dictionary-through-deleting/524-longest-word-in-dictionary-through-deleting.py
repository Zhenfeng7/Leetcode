class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result = ""
        for i in dictionary:
            if self._isSubsequence(i, s):
                if len(i) > len(result):
                    result = i
                elif len(i) == len(result):
                    result = min(result, i)
                
                
        return result
                
        
        
        
    def _isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        ps, pt = 0, 0
        while pt < len(t) and ps < len(s):
            if s[ps] == t[pt]:
                
                ps += 1
                pt += 1
            else:
                pt += 1
        return ps == len(s)