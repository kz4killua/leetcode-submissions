func reverseBits(n int) int {
    result := 0
    for i := 0; i < 32; i++ {
        if ((1 << i) & n) > 0 {
            result |= 1 << (31 - i)
        }
    }
    return result
}
