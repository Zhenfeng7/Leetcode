class Solution(object):
    
    char_map = ["0","1","abc", "def", "ghi", "jkl","mno", "pqrs", "tuv", "wxyz"]
    
    def _helper(self, digits, prefix, index, ans):
        if index == len(digits):
            ans.append(prefix)
            return
        else:
            num = int(digits[index])
            letter = self.char_map[num]
            for c in letter:
                self._helper(digits, prefix + c, index + 1, ans)

    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lst = []
        if len(digits) == 0:
            return lst
        self._helper(digits, "", 0, lst)
        return lst
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        