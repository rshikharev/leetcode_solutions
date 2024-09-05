[Sliding Window Approach to Maximize Contiguous 1's After Removing One Element on LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solutions/5743089/sliding-window-approach-on-time-o1-space-complexity/)

# Intuition
To solve the problem of finding the longest subarray containing only 1's after deleting exactly one element, I first considered the idea of using a sliding window approach. The goal is to find the longest contiguous subarray of 1's that can be achieved by allowing at most one zero in the subarray.

# Approach
We use a sliding window approach with two pointers, `left` and `right`, to keep track of the current subarray. As we iterate through the array with the `right` pointer, we count the number of zeros in the current window. If there is more than one zero, we move the `left` pointer to shrink the window until there is at most one zero left. During this process, we keep track of the maximum length of subarrays that contain at most one zero. 

After processing the entire array, if the maximum length equals the length of the array and there were no zeros, we subtract one from the result since we must remove one element.

# Complexity
- Time complexity: $$O(n)$$
- Space complexity: $$O(1)$$

### Example Analysis
1. **Example 1**: `nums = [1,1,0,1]`
   - Initial window: `[1,1,0,1]`
   - Remove the zero at index 2: `[1,1,1]`
   - Longest subarray of 1's after removing one element: 3

2. **Example 2**: `nums = [0,1,1,1,0,1,1,0,1]`
   - Initial window: `[0,1,1,1,0,1,1,0,1]`
   - Remove the zero at index 4: `[0,1,1,1,1,1,0,1]`
   - Longest subarray of 1's after removing one element: 5

3. **Example 3**: `nums = [1,1,1]`
   - The array contains only 1's.
   - Remove one element: `[1,1]`
   - Longest subarray of 1's after removing one element: 2

I welcome any feedback or suggestions on how to further optimize the code.

# Code
```python3 []
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        left = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # Move the left pointer to ensure there is at most one zero in the window
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the maximum length of the subarray containing only ones
            max_len = max(max_len, right - left)
        
        # If the array contains only ones, we need to remove one element
        return max_len if zero_count == 1 or max_len < len(nums) else max_len - 1
```
