"""
Problem 1: Find Words
Given an array of strings words, write a function findWords that returns 
the words that can be typed using letters of the alphabet on only one row of American 
keyboard.

The American keyboard rows:
- First row: "qwertyuiop"
- Second row: "asdfghjkl" 
- Third row: "zxcvbnm"

Note: Case-insensitive - both lowercased and uppercased letters are treated the same.
"""

def findWords(words):
    """
    Find words that can be typed using only one row of American keyboard.
    
    Args:
        words: List of strings to check
        
    Returns:
        List of words that can be typed using only one keyboard row
    """
    # Define keyboard rows
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
    
    result = []
    
    for word in words:
        # Convert to lowercase for case-insensitive comparison
        word_lower = word.lower()
        
        # Check if all characters belong to the same row
        if all(char in row1 for char in word_lower):
            result.append(word)
        elif all(char in row2 for char in word_lower):
            result.append(word)
        elif all(char in row3 for char in word_lower):
            result.append(word)
    
    return result


# Test cases
def test_findWords():
    # Example 1
    words1 = ["Hello","Alaska","Dad","Peace"]
    result1 = findWords(words1)
    print(f"Input: {words1}")
    print(f"Output: {result1}")
    print(f"Expected: ['Alaska','Dad']")
    print()
    
    # Example 2
    words2 = ["omk"]
    result2 = findWords(words2)
    print(f"Input: {words2}")
    print(f"Output: {result2}")
    print(f"Expected: []")
    print()
    
    # Example 3
    words3 = ["adsdf","sfd"]
    result3 = findWords(words3)
    print(f"Input: {words3}")
    print(f"Output: {result3}")
    print(f"Expected: ['adsdf','sfd']")
    print()


if __name__ == "__main__":
    test_findWords()
