class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        l = r = 0
        output = 1
        seen = {s[0]}

        while r < (len(s) - 1):
            r += 1

            if s[r] in seen:
                # Advance the left pointer to remove repeats
                while (s[r] in seen):
                    seen.remove(s[l])
                    l += 1

            seen.add(s[r])
            # Update the longest substring
            output = max(output, r - l + 1)

        return output
