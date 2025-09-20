def _coin_change(coins: List[int], amount: int, memo: dict):

    if amount == 0:
        return 0
    
    if amount not in memo:
    
        output = -1
        for denomination in coins:
            change = amount - denomination
            if change < 0:
                continue

            result = _coin_change(coins, change, memo)
            if result == -1:
                continue

            if output == -1:
                output = 1 + result
            else:
                output = min(output, 1 + result)

        memo[amount] = output

    return memo[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        return _coin_change(coins, amount, memo)
