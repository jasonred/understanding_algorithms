"""
Problem 1: Two Sum for Sorted Array
Write a python function two_sum that takes an array of sorted numbers 
nums and an integer target as input, return the indices i and j such that nums[i] + 
nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy 
the condition.
Return the answer with the smaller index first.
"""

def two_sum(nums, target):
    """
    Find two numbers in sorted array that sum to target
    Returns indices [i, j] where nums[i] + nums[j] == target and i < j
    Returns [] if no such pair exists
    
    Args:
        nums: List of sorted integers
        target: Target sum
    
    Returns:
        List of two indices [i, j] if found, empty list otherwise
    """
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [3, 4, 5, 6]
    target1 = 7
    result1 = two_sum(nums1, target1)
    print(f"Example 1:")
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print()
    
    # Test case 2
    nums2 = [-4, -3, 5, 6]
    target2 = 7
    result2 = two_sum(nums2, target2)
    print(f"Example 2:")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print()
    
    # Additional test cases
    nums3 = [1, 2, 3, 4, 5]
    target3 = 8
    result3 = two_sum(nums3, target3)
    print(f"Additional test:")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
