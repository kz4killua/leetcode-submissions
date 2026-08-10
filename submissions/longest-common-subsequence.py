class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return _longest_common_subsequence(text1, text2, 0, 0, len(text1), len(text2), dict())


def _longest_common_subsequence(
    text1: str, text2: str, p1: int, p2: int, l1: int, l2: int, memo: dict
):

    if p1 >= l1 or p2 >= l2:
        return 0

    if (p1, p2) in memo:
        return memo[p1, p2]

    if text1[p1] == text2[p2]:
        memo[p1, p2] = 1 + _longest_common_subsequence(text1, text2, p1 + 1, p2 + 1, l1, l2, memo)
        return memo[p1, p2]

    memo[p1, p2] = max(
        _longest_common_subsequence(text1, text2, p1 + 1, p2, l1, l2, memo),
        _longest_common_subsequence(text1, text2, p1, p2 + 1, l1, l2, memo),
    )
    return memo[p1, p2]
