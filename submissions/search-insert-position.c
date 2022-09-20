int searchInsert(int* nums, int numsSize, int target){

    // Stop when there are no values left to search
    if (numsSize == 0)
    {
        return 0;
    }

    int m = numsSize / 2;

    if (nums[m] == target)
    {
        return m;
    }
    else if (nums[m] > target)
    {
        return searchInsert(nums, m, target);
    }
    else
    {
        return m + searchInsert(&nums[m + 1], numsSize - (m + 1), target) + 1;
    }
}
