

int removeDuplicates(int* nums, int numsSize){
    
    // Keep a pointer to the next unique slot
    short next = 0;
    // Keep track of the last encountered (unique) element
    short last = -101;
    
    for (short i = 0; i < numsSize; i++)
    {
        // Check for non-duplicates
        if (nums[i] != last)
        {
            // Move the number into place
            nums[next] = nums[i];
            // Update the last encountered (unique) element
            last = nums[i];
            // Update the pointer to the next unique slot
            next++;
        }
    }
    return next;
}
