def word_break(s: str, start: int, wordDict: List[str], memo: dict):

    if start == len(s):
        return True

    if start not in memo:

        memo[start] = False
    
        for word in wordDict:

            # Check if s[start:] starts with word
            if (len(s) - start) < len(word):
                continue

            is_prefix = True
            for i in range(len(word)):
                if s[start + i] != word[i]:
                    is_prefix = False
                    break

            # Call recursively with the new start index
            if is_prefix:
                if word_break(s, start + len(word), wordDict, memo):
                    memo[start] = True
                    break

    return memo[start]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = dict()
        return word_break(s, 0, wordDict, memo)
