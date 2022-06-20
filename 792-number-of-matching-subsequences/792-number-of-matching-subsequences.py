class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        hashmap = {}
        for word in words:
            if word not in hashmap:
                if self._isSubsequence(word, s):
                    hashmap[word] = True
                    count += 1
                else:
                    hashmap[word] = False
            else:
                count += hashmap[word]
        return count
        
        
    def _isSubsequence(self, sub: str, t: str) -> bool:
        if len(sub) > len(t):
            return False
        
        ps, pt = 0, 0
        while pt < len(t) and ps < len(sub):
            if ps == len(sub): return True
            if sub[ps] == t[pt]:
                
                ps += 1
                pt += 1
            else:
                pt += 1
        return ps == len(sub)