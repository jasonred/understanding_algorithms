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
    # Step 1: Create a dictionary to map each character to its position in the alien alphabet
    # For example, if order = "hlabcdefgijkmnopqrstuvwxyz"
    # Then 'h' is at position 0, 'l' is at position 1, 'a' is at position 2, etc.
    char_to_order = {}
    for i in range(len(order)):
        char_to_order[order[i]] = i
    
    # Step 2: Compare each pair of adjacent words
    # We need to check if words[0] <= words[1] <= words[2] <= ... <= words[n-1]
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        
        # If any pair is not in order, the whole list is not sorted
        if not are_words_in_order(current_word, next_word, char_to_order):
            return False
    
    # If we checked all pairs and they were all in order, the list is sorted
    return True


def are_words_in_order(word1, word2, char_to_order):
    """
    Check if word1 comes before or is equal to word2 according to alien alphabet order.
    
    Args:
        word1: First word
        word2: Second word  
        char_to_order: Dictionary mapping characters to their order
        
    Returns:
        True if word1 <= word2, False otherwise
    """
    # Find the length of the shorter word so we don't go out of bounds
    shorter_length = len(word1)
    if len(word2) < shorter_length:
        shorter_length = len(word2)
    
    # Compare each character position by position
    for i in range(shorter_length):
        char1 = word1[i]
        char2 = word2[i]
        
        # Get the order of each character in the alien alphabet
        order1 = char_to_order[char1]
        order2 = char_to_order[char2]
        
        # If word1's character comes before word2's character, word1 is smaller
        if order1 < order2:
            return True
        # If word1's character comes after word2's character, word1 is larger
        elif order1 > order2:
            return False
        # If characters are equal, we need to check the next character
        # (this is handled by the loop continuing)
    
    # If we've compared all characters and they were all equal,
    # the shorter word comes first (or they're the same length)
    return len(word1) <= len(word2)


# Test cases
def test_isAlienSorted():
    print("=== Testing isAlienSorted function ===\n")
    
    # Test Case 1: Words that are NOT sorted
    print("Test 1: Checking if words are sorted")
    words1 = ["word", "world", "row"]
    order1 = "worldabcefghijkmnpqstuvxyz"
    result1 = isAlienSorted(words1, order1)
    print(f"Words: {words1}")
    print(f"Alien alphabet order: '{order1}'")
    print(f"Are words sorted? {result1}")
    print(f"Expected: False (because 'word' should come after 'world')")
    print()
    
    # Test Case 2: Words that are NOT sorted (shorter word after longer)
    print("Test 2: Checking shorter word after longer word")
    words2 = ["apple", "app"]
    order2 = "abcdefghijklmnopqrstuvwxyz"
    result2 = isAlienSorted(words2, order2)
    print(f"Words: {words2}")
    print(f"Alien alphabet order: '{order2}' (normal English order)")
    print(f"Are words sorted? {result2}")
    print(f"Expected: False (because 'apple' is longer than 'app', so 'app' should come first)")
    print()
    
    # Test Case 3: Words that ARE sorted
    print("Test 3: Checking correctly sorted words")
    words3 = ["hello", "leetcode"]
    order3 = "hlabcdefgijkmnopqrstuvwxyz"
    result3 = isAlienSorted(words3, order3)
    print(f"Words: {words3}")
    print(f"Alien alphabet order: '{order3}'")
    print(f"Are words sorted? {result3}")
    print(f"Expected: True (because 'h' comes before 'l' in this alien alphabet)")
    print()
    
    # Test Case 4: Simple example with normal alphabet
    print("Test 4: Simple example with normal alphabet")
    words4 = ["cat", "dog", "elephant"]
    order4 = "abcdefghijklmnopqrstuvwxyz"
    result4 = isAlienSorted(words4, order4)
    print(f"Words: {words4}")
    print(f"Alien alphabet order: '{order4}' (normal English order)")
    print(f"Are words sorted? {result4}")
    print(f"Expected: True (because 'cat' < 'dog' < 'elephant' alphabetically)")
    print()


if __name__ == "__main__":
    test_isAlienSorted()
