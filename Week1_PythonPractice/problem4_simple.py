"""
Problem 4: Is Alien Sorted - Simple Version
Using for word in words and for char in word style
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
    # Go through each word in the list
    i = 0
    for word1 in words:
        # Make sure we don't go past the last word
        if i < len(words) - 1:
            word2 = words[i + 1]
            
            # Go through each character in the first word
            j = 0
            for char1 in word1:
                # Make sure we don't go past the end of the second word
                if j >= len(word2):
                    break
                    
                char2 = word2[j]
                
                # Find where each character appears in the alien alphabet
                position1 = order.find(char1)
                position2 = order.find(char2)
                
                # If first word's character comes after second word's character, not sorted
                if position1 > position2:
                    return False
                # If first word's character comes before second word's character, they're sorted
                elif position1 < position2:
                    break
                # If characters are the same, check the next character
                
                # Move to the next character
                j = j + 1
            
            # If all characters were the same, shorter word should come first
            if len(word1) > len(word2):
                return False
        
        # Move to the next word
        i = i + 1
    
    # If we checked all word pairs and they were all in order, the list is sorted
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
