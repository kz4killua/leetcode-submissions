class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = str()
        
        for chars in zip(*strs):
            # Make sure all the characters are the same
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break
            
        return prefix
