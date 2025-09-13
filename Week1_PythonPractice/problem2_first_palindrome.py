"""
Problem 2: First Palindrome
Given an array of strings words, write a function firstPalindrome that 
returns the first palindromic string in the array. If there is no such string, 
return an empty string "".

A string is palindromic if it reads the same forward and backward.
"""

def firstPalindrome(words):
    """
    Find the first palindromic string in the array.
    
    Args:
        words: List of strings to check
        
    Returns:
        First palindromic string, or empty string if none found
    """
    for word in words:
        if is_palindrome(word):
            return word
    return ""


def is_palindrome(word):
    """
    Check if a string is palindromic.
    
    Args:
        word: String to check
        
    Returns:
        True if palindromic, False otherwise
    """
    left = 0
    right = len(word) - 1
    
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    
    return True


# Test cases
def test_firstPalindrome():
    # Example 1
    words1 = ["abc","car","ada","racecar","cool"]
    result1 = firstPalindrome(words1)
    print(f"Input: {words1}")
    print(f"Output: '{result1}'")
    print(f"Expected: 'ada'")
    print()
    
    # Example 2
    words2 = ["notapalindrome","racecar"]
    result2 = firstPalindrome(words2)
    print(f"Input: {words2}")
    print(f"Output: '{result2}'")
    print(f"Expected: 'racecar'")
    print()
    
    # Example 3
    words3 = ["def","ghi"]
    result3 = firstPalindrome(words3)
    print(f"Input: {words3}")
    print(f"Output: '{result3}'")
    print(f"Expected: ''")
    print()


if __name__ == "__main__":
    test_firstPalindrome()
