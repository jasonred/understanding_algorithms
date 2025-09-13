"""
Problem 5: Most Common Word
Given a string paragraph and a string array of the banned words banned,
write a function mostCommonWord, that returns the most frequent word that is not 
banned. It is guaranteed there is at least one word that is not banned, and that the 
answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in 
lowercase.
"""

import re
from collections import Counter


def mostCommonWord(paragraph, banned):
    """
    Find the most frequent word that is not banned.
    
    Args:
        paragraph: String containing words
        banned: List of banned words
        
    Returns:
        Most frequent non-banned word in lowercase
    """
    # Convert banned words to lowercase for case-insensitive comparison
    banned_set = set(word.lower() for word in banned)
    
    # Extract words from paragraph (remove punctuation, convert to lowercase)
    words = re.findall(r'\b\w+\b', paragraph.lower())
    
    # Count word frequencies
    word_count = Counter(words)
    
    # Find the most common non-banned word
    max_count = 0
    most_common = ""
    
    for word, count in word_count.items():
        if word not in banned_set and count > max_count:
            max_count = count
            most_common = word
    
    return most_common


# Test cases
def test_mostCommonWord():
    # Example 1
    paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned1 = ["hit"]
    result1 = mostCommonWord(paragraph1, banned1)
    print(f"Input: paragraph = '{paragraph1}', banned = {banned1}")
    print(f"Output: '{result1}'")
    print(f"Expected: 'ball'")
    print()
    
    # Example 2
    paragraph2 = "a."
    banned2 = []
    result2 = mostCommonWord(paragraph2, banned2)
    print(f"Input: paragraph = '{paragraph2}', banned = {banned2}")
    print(f"Output: '{result2}'")
    print(f"Expected: 'a'")
    print()
    
    # Additional test case
    paragraph3 = "The quick brown fox jumps over the lazy dog. The fox is quick."
    banned3 = ["the", "fox"]
    result3 = mostCommonWord(paragraph3, banned3)
    print(f"Input: paragraph = '{paragraph3}', banned = {banned3}")
    print(f"Output: '{result3}'")
    print(f"Expected: 'quick'")
    print()


if __name__ == "__main__":
    test_mostCommonWord()
