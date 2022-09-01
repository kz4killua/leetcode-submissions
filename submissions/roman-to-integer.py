class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        length = len(s)
        
        for i in range(length):
            
            current = values[s[i]]
            if i + 1 < length:
                next = values[s[i + 1]]
                
                if next > current:
                    result -= current
                    continue
                    
            result += current
            
        return result
