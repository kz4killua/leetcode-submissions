class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = dict()

        return min(
            min_cost(0, cost, memo),
            min_cost(1, cost, memo),
        )


def min_cost(i: int, cost: list[int], memo: dict):
    if i >= len(cost):
        return 0

    if i not in memo:
        memo[i] = cost[i] + min(
            min_cost(i + 1, cost, memo),
            min_cost(i + 2, cost, memo),
        )

    return memo[i]
