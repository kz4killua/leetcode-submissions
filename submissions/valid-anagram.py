class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counts = dict()

        for c in s:
            counts.setdefault(c, 0)
            counts[c] += 1

        for c in t:
            if c not in counts:
                return False
            counts[c] -= 1
        
        for value in counts.values():
            if value != 0:
                return False

        return True
