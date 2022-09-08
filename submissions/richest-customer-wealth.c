

int maximumWealth(int** accounts, int accountsSize, int* accountsColSize){
    int max_wealth = 0;
    
    // Go to each customer
    for (int i = 0; i < accountsSize; i++)
    {
        // Sum up the money in each of their accounts
        int wealth = 0;
        for (int j = 0; j < *accountsColSize; j++) {
            wealth += accounts[i][j];
        }
        // Check if their wealth is greater than the maximum wealth
        if (wealth > max_wealth) {
            max_wealth = wealth; 
        }
    }
    return max_wealth;
}
