def firstUniqChar(s: str) -> int:
    """
    Find the index of the first character that appears exactly once.
    
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1) - at most 26 characters for lowercase letters
    
    Args:
        s: Input string (lowercase)
        
    Returns:
        int: Index of first unique character, or -1 if none exists
    """
    if not s:
        return -1
    
    # Count occurrences of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first character with count == 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1

def firstUniqChar_optimized(s: str) -> int:
    """
    Alternative implementation using collections.Counter for cleaner code.
    Same time and space complexity.
    """
    from collections import Counter
    
    if not s:
        return -1
    
    # Count occurrences
    char_count = Counter(s)
    
    # Find first unique character
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1

def firstUniqChar_with_queue(s: str) -> int:
    """
    Implementation using a queue to track candidate indices.
    This approach can be more efficient for very long strings with many duplicates.
    """
    if not s:
        return -1
    
    char_count = {}
    queue = []
    
    for i, char in enumerate(s):
        if char not in char_count:
            char_count[char] = 1
            queue.append(i)
        else:
            char_count[char] += 1
            # Remove indices from queue if character appears more than once
            while queue and char_count[s[queue[0]]] > 1:
                queue.pop(0)
    
    return queue[0] if queue else -1

# Test cases
def test_first_unique_char():
    """Test the implementation with various cases."""
    
    # Test case 1: "leetcode" -> 0 (first 'l' is unique)
    test1 = "leetcode"
    result1 = firstUniqChar(test1)
    print(f"Test 1: '{test1}' -> {result1} (expected: 0)")
    
    # Test case 2: "loveleetcode" -> 2 (first 'v' is unique)
    test2 = "loveleetcode"
    result2 = firstUniqChar(test2)
    print(f"Test 2: '{test2}' -> {result2} (expected: 2)")
    
    # Test case 3: "aabb" -> -1 (no unique characters)
    test3 = "aabb"
    result3 = firstUniqChar(test3)
    print(f"Test 3: '{test3}' -> {result3} (expected: -1)")
    
    # Test case 4: "a" -> 0 (single character is unique)
    test4 = "a"
    result4 = firstUniqChar(test4)
    print(f"Test 4: '{test4}' -> {result4} (expected: 0)")
    
    # Test case 5: "" -> -1 (empty string)
    test5 = ""
    result5 = firstUniqChar(test5)
    print(f"Test 5: '{test5}' -> {result5} (expected: -1)")
    
    # Test case 6: "abccba" -> -1 (all characters appear twice)
    test6 = "abccba"
    result6 = firstUniqChar(test6)
    print(f"Test 6: '{test6}' -> {result6} (expected: -1)")
    
    # Test case 7: "abcdef" -> 0 (all characters are unique, first one)
    test7 = "abcdef"
    result7 = firstUniqChar(test7)
    print(f"Test 7: '{test7}' -> {result7} (expected: 0)")

# Test all implementations
def test_all_implementations():
    """Test all three implementations to ensure they produce the same results."""
    test_cases = ["leetcode", "loveleetcode", "aabb", "a", "", "abccba", "abcdef"]
    
    print("Testing all implementations:")
    print("=" * 50)
    
    for test_case in test_cases:
        result1 = firstUniqChar(test_case)
        result2 = firstUniqChar_optimized(test_case)
        result3 = firstUniqChar_with_queue(test_case)
        
        print(f"'{test_case}': {result1}, {result2}, {result3} - {'✓' if result1 == result2 == result3 else '✗'}")

if __name__ == "__main__":
    print("First Unique Character Tests")
    print("=" * 40)
    test_first_unique_char()
    print("\n")
    test_all_implementations()
