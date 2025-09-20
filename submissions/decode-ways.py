def _num_decodings(s: str, start: int, decodings: set, memo: dict):

    if start == len(s):
        return 1
    
    if start not in memo:
        
        count = 0
        
        # Try grouping the first digit only
        if len(s) - start >= 1:
            prefix = s[start : start + 1]
            if (prefix in decodings):
                count += _num_decodings(s, start + 1, decodings, memo)
        
        # Try grouping the first two digits
        if len(s) - start >= 2:
            prefix = s[start : start + 2]
            if (prefix in decodings):
                count += _num_decodings(s, start + 2, decodings, memo)
        
        memo[start] = count
        
    return memo[start]

class Solution:
    def numDecodings(self, s: str) -> int:
        
        # Initialize the decodings
        decodings = set()
        for i in range(1, 27):
            decodings.add(str(i))

        memo = dict()
        return _num_decodings(s, 0, decodings, memo)
