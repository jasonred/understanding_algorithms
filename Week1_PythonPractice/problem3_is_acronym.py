"""
Problem 3: Is Acronym
Given an array of strings words and a string s, determine if s is an 
acronym of words. The string s is considered an acronym of words if it can be 
formed by concatenating the first character of each string in words in order.

For example, "ab" can be formed from ["apple", "banana"], but it can't be 
formed from ["bear", "aardvark"].
"""

def isAcronym(words, s):
    """
    Check if string s is an acronym of words array.
    
    Args:
        words: List of strings
        s: String to check if it's an acronym
        
    Returns:
        True if s is an acronym of words, False otherwise
    """
    # Check if lengths match
    if len(words) != len(s):
        return False
    
    # Check if each character in s matches the first character of corresponding word
    for i in range(len(words)):
        if len(words[i]) == 0:  # Handle empty strings
            return False
        if words[i][0] != s[i]:
            return False
    
    return True


# Test cases
def test_isAcronym():
    # Example 1
    words1 = ["alice","bob","charlie"]
    s1 = "abc"
    result1 = isAcronym(words1, s1)
    print(f"Input: words = {words1}, s = '{s1}'")
    print(f"Output: {result1}")
    print(f"Expected: True")
    print()
    
    # Example 2
    words2 = ["an","apple"]
    s2 = "a"
    result2 = isAcronym(words2, s2)
    print(f"Input: words = {words2}, s = '{s2}'")
    print(f"Output: {result2}")
    print(f"Expected: False")
    print()
    
    # Example 3
    words3 = ["never","gonna","give","up","on","you"]
    s3 = "ngguoy"
    result3 = isAcronym(words3, s3)
    print(f"Input: words = {words3}, s = '{s3}'")
    print(f"Output: {result3}")
    print(f"Expected: True")
    print()


if __name__ == "__main__":
    test_isAcronym()
