def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Find the next greater element for each element in nums1.
    
    Args:
        nums1: Subset array of nums2
        nums2: The larger array containing all elements from nums1
        
    Returns:
        List of next greater elements for each element in nums1, -1 if not found
    """
    # Use a monotonic decreasing stack to find next greater element for each element in nums2
    stack = []
    next_greater = {}  # Map each element to its next greater element
    
    # Process nums2 from left to right
    for num in nums2:
        # While stack is not empty and current element is greater than stack top
        while stack and num > stack[-1]:
            # The next greater element for stack top is current element
            next_greater[stack.pop()] = num
        # Push current element to stack
        stack.append(num)
    
    # For remaining elements in stack, no greater element exists
    while stack:
        next_greater[stack.pop()] = -1
    
    # Map results for nums1 using O(1) lookups
    result = []
    for num in nums1:
        result.append(next_greater[num])
    
    return result


# Test with the provided example
if __name__ == "__main__":
    # Example 1
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    result = nextGreaterElement(nums1, nums2)
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {result}")
    print(f"Expected: [-1, 3, -1]")
    print(f"Correct: {result == [-1, 3, -1]}")
    
    # Additional test cases
    print("\nAdditional test cases:")
    
    # Test case 2
    nums1_2 = [2, 4]
    nums2_2 = [1, 2, 3, 4]
    result2 = nextGreaterElement(nums1_2, nums2_2)
    print(f"nums1 = {nums1_2}, nums2 = {nums2_2} -> {result2}")
    
    # Test case 3
    nums1_3 = [1, 3, 2]
    nums2_3 = [3, 1, 2, 4]
    result3 = nextGreaterElement(nums1_3, nums2_3)
    print(f"nums1 = {nums1_3}, nums2 = {nums2_3} -> {result3}")
