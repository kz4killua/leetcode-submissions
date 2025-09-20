def _climb_stairs(n: int, memo: dict = None):
    
    if n not in memo:
    
        output = 0
        if n >= 2:
            output += _climb_stairs(n - 2, memo)
        if n >= 1:
            output += _climb_stairs(n - 1, memo)

        memo[n] = output

    return memo[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize the memo with the base case
        memo = {0: 1}
        return _climb_stairs(n, memo)
