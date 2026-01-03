func countBits(n int) []int {
    dp := make([]int, n + 1)
    offset := 1

    for i := 1; i <= n; i++ {
        // Update the offset when necessary
        if i == offset * 2 {
            offset *= 2
        }
        // Compute the recurrence relation
        dp[i] = 1 + dp[i - offset]
    }

    return dp
}
