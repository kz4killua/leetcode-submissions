#include <string.h>


int climbStairs(int n) {
    
    // Create an array to store results
    int results[46];
    memset(results, 0, sizeof(results));

    // Run the function
    int output = climbStairsRecursive(n, results);

    return output;
}


int climbStairsRecursive(int n, int results[]){

    // Base case: No more steps
    if (n == 0) {
        return 1;
    }
    // Base case: Value has been computed previously
    if (results[n] != 0) {
        return results[n];
    }

    int output = 0;

    // Call function recursively, trying one and two steps
    if (n >= 1) {
        output += climbStairsRecursive(n - 1, results);
    }
    if (n >= 2) {
        output += climbStairsRecursive(n - 2, results);
    }

    // Store results to avoid recomputation
    results[n] = output;

    return output;
}
