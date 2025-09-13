def NumHi(state):
    """
    Count the number of 'hi's said when students pass each other in a hallway.
    
    Args:
        state (str): String representing hallway state where:
            '>' = student moving right
            '<' = student moving left  
            '-' = empty space
            
    Returns:
        int: Number of times students say 'hi' when passing each other
    """
    count = 0
    
    # Count interactions between all pairs of students
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            # If student at i is moving right and student at j is moving left
            if state[i] == '>' and state[j] == '<':
                count += 2  # Both students say hi
    
    return count


# Test cases
if __name__ == "__main__":
    # Test Example 1
    state1 = ">---<<"
    result1 = NumHi(state1)
    print(f"Input: '{state1}'")
    print(f"Output: {result1}")
    print()
    
    # Test Example 2
    state2 = "><>---<"
    result2 = NumHi(state2)
    print(f"Input: '{state2}'")
    print(f"Output: {result2}")
    print()
    
    # Additional test cases
    test_cases = [
        "",           # Empty hallway
        ">",          # Single student right
        "<",          # Single student left
        "><",         # Two students passing
        ">>",         # Two students same direction
        "<<",         # Two students same direction
        ">-<",        # Students with space between
        ">><<",       # Multiple students
        ">--<--<",    # Students with multiple spaces
        "><><",       # Alternating students
    ]
    
    print("Additional test cases:")
    for state in test_cases:
        result = NumHi(state)
        print(f"Input: '{state}' -> Output: {result}")
    
    # Let's trace through Example 1 to verify
    print("\nTracing Example 1: '>---<<'")
    state = ">---<<"
    print("Positions: 012345")
    print(f"State:    {state}")
    print("Student at position 0 (>) will pass students at positions 4 and 5 (<)")
    print("Total interactions: 2")
    print(f"Function result: {NumHi(state)}")
