def _count_substrings(s: str, l: int, r: int):

    count = 0
    while True:
        if s[l] != s[r]:
            break

        count += 1
        l -= 1
        r += 1

        # Ensure l and r remain within the string
        if not (0 <= l <= r < len(s)):
            break

    return count


class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        for center in range(0, len(s)):
            # Count all odd palindromic substrings
            count += _count_substrings(s, center, center)
            # Count all even palindromic substrings
            if (center + 1 < len(s)):
                count += _count_substrings(s, center, center + 1)

        return count
