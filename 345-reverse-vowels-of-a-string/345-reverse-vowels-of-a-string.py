class Solution:
    
    def reverseVowels(self, s: str) -> str:
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        lo = 0
        hi = len(s) - 1
        lst = list(s)
        
        while lo < hi:
            if lst[lo].lower() in VOWELS and lst[hi].lower() in VOWELS:
                lst[lo], lst[hi] = lst[hi], lst[lo]
                lo += 1
                hi -= 1
            else:
                if lst[lo].lower() not in VOWELS: lo += 1
                if lst[hi].lower() not in VOWELS: hi -= 1
        return ''.join(lst)