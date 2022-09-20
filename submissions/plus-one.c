

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){
    
    // Create a new array big enough for 1 extra digit
    int *output = malloc((digitsSize + 1) * sizeof(int));
    
    int carry = 1;
    *returnSize = digitsSize;
    for (int i = digitsSize; i >= 0; i--)
    {   
        // Compute the sum
        int sum;
        if (i > 0)
        {
            sum = digits[i - 1] + carry;
        }
        else
        {
            sum = carry;
        }
        // Carry over extra digits
        if (sum >= 10)
        {
            sum -= 10;
            carry = 1;
        }
        else
        {
            carry = 0;
        }
        // Update the output
        output[i] = sum;
    }
    

    // Move the pointer to the first array element
    if (output[0] == 0)
    {
        *returnSize = digitsSize;
        output = &output[1];
    }
    else
    {
        *returnSize = digitsSize + 1;
    }
    
    return output;
}
