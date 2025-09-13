"""
Problem 4: Is Alien Sorted
In an alien language, surprisingly, they also use English lowercase letters, 
but possibly in a different order. The order of the alphabet is some 
permutation of lowercase letters.

Write a function isAlienSorted that takes a sequence of words written in the 
alien language, and the order of the alphabet as input, return true if and only 
if the given words are sorted lexicographically in this alien language.
"""

def isAlienSorted(words, order):
    """
    Check if words are sorted lexicographically in alien language order.
    
    Args:
        words: List of words in alien language
        order: String representing the alien alphabet order
        
    Returns:
        True if words are sorted, False otherwise
    """
    # Create a mapping from character to its position in the alien alphabet
    char_to_order = {char: i for i, char in enumerate(order)}
    
    # Compare adjacent words
    for i in range(len(words) - 1):
        if not is_less_or_equal(words[i], words[i + 1], char_to_order):
            return False
    
    return True


def is_less_or_equal(word1, word2, char_to_order):
    """
    Check if word1 <= word2 according to alien alphabet order.
    
    Args:
        word1: First word
        word2: Second word
        char_to_order: Dictionary mapping characters to their order
        
    Returns:
        True if word1 <= word2, False otherwise
    """
    min_len = min(len(word1), len(word2))
    
    # Compare character by character
    for i in range(min_len):
        order1 = char_to_order[word1[i]]
        order2 = char_to_order[word2[i]]
        
        if order1 < order2:
            return True
        elif order1 > order2:
            return False
        # If equal, continue to next character
    
    # If all compared characters are equal, shorter word comes first
    return len(word1) <= len(word2)


# Test cases
def test_isAlienSorted():
    # Example 1
    words1 = ["word","world","row"]
    order1 = "worldabcefghijkmnpqstuvxyz"
    result1 = isAlienSorted(words1, order1)
    print(f"Input: words = {words1}, order = '{order1}'")
    print(f"Output: {result1}")
    print(f"Expected: False")
    print()
    
    # Example 2
    words2 = ["apple","app"]
    order2 = "abcdefghijklmnopqrstuvwxyz"
    result2 = isAlienSorted(words2, order2)
    print(f"Input: words = {words2}, order = '{order2}'")
    print(f"Output: {result2}")
    print(f"Expected: False")
    print()
    
    # Additional test case - sorted words
    words3 = ["hello","leetcode"]
    order3 = "hlabcdefgijkmnopqrstuvwxyz"
    result3 = isAlienSorted(words3, order3)
    print(f"Input: words = {words3}, order = '{order3}'")
    print(f"Output: {result3}")
    print(f"Expected: True")
    print()


if __name__ == "__main__":
    test_isAlienSorted()
