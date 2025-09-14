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
        word1 = words[i]
        word2 = words[i + 1]
        
        # Step 3: Compare these two words character by character
        # Find the length of the shorter word so we don't go out of bounds
        shorter_length = len(word1)
        if len(word2) < shorter_length:
            shorter_length = len(word2)
        
        # Compare each character position by position
        for j in range(shorter_length):
            char1 = word1[j]
            char2 = word2[j]
            
            # Get the order of each character in the alien alphabet
            order1 = char_to_order[char1]
            order2 = char_to_order[char2]
            
            # If word1's character comes after word2's character, they're not in order
            if order1 > order2:
                return False
            # If word1's character comes before word2's character, they are in order
            elif order1 < order2:
                break
            # If characters are equal, we need to check the next character
            # (this is handled by the loop continuing)
        
        # If we've compared all characters and they were all equal,
        # check if the first word is shorter or equal length
        if len(word1) > len(word2):
            return False
    
    # If we checked all pairs and they were all in order, the list is sorted
    return True


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
