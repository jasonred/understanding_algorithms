"""
Problem 6: Shortest Distance to Character
Given a string s and a character c that occurs in s, return an array of 
integers answer where answer.length == s.length and answer[i] is the distance 
from index i to the closest occurrence of character c in s.

Both s and c are lowercase english letters and it is guaranteed that c occurs 
at least once in s.

The distance between two indices i and j is abs(i - j), where abs is the 
absolute value function.
"""

def shortestToChar(s, c):
    """
    Find shortest distance from each character to the closest occurrence of c.
    
    Args:
        s: Input string
        c: Character to find distances to
        
    Returns:
        List of distances from each position to closest occurrence of c
    """
    n = len(s)
    result = [0] * n
    
    # First pass: find distances from left to right
    prev = float('-inf')
    for i in range(n):
        if s[i] == c:
            prev = i
        result[i] = i - prev
    
    # Second pass: find distances from right to left and take minimum
    prev = float('inf')
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            prev = i
        result[i] = min(result[i], prev - i)
    
    return result


# Alternative solution using two separate loops
def shortestToChar_alternative(s, c):
    """
    Alternative implementation using separate left and right passes.
    """
    n = len(s)
    result = [float('inf')] * n
    
    # Find all positions of character c
    c_positions = [i for i in range(n) if s[i] == c]
    
    # For each position, find minimum distance to any c position
    for i in range(n):
        for pos in c_positions:
            result[i] = min(result[i], abs(i - pos))
    
    return result


# Test cases
def test_shortestToChar():
    # Example 1
    s1 = "loveleetcode"
    c1 = "e"
    result1 = shortestToChar(s1, c1)
    expected1 = [3,2,1,0,1,0,0,1,2,2,1,0]
    print(f"Input: s = '{s1}', c = '{c1}'")
    print(f"Output: {result1}")
    print(f"Expected: {expected1}")
    print(f"Correct: {result1 == expected1}")
    print()
    
    # Example 2
    s2 = "aaab"
    c2 = "b"
    result2 = shortestToChar(s2, c2)
    expected2 = [3,2,1,0]
    print(f"Input: s = '{s2}', c = '{c2}'")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    print(f"Correct: {result2 == expected2}")
    print()
    
    # Additional test case
    s3 = "abaa"
    c3 = "b"
    result3 = shortestToChar(s3, c3)
    expected3 = [1,0,1,2]
    print(f"Input: s = '{s3}', c = '{c3}'")
    print(f"Output: {result3}")
    print(f"Expected: {expected3}")
    print(f"Correct: {result3 == expected3}")
    print()


if __name__ == "__main__":
    test_shortestToChar()
