

int removeElement(int* nums, int numsSize, int val){
    
    int occurrences = 0;
    
    for (int i = 0; i < numsSize; i++)
    {
        // Keep track of how many times we have seen `val`
        if (nums[i] == val)
        {
            occurrences++;
            continue;
        }
        // Place each element in its proper place
        nums[i - occurrences] = nums[i];
    }
    
    int k = numsSize - occurrences;
    return k;
}
