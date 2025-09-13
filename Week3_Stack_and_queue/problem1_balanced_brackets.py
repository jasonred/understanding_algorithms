def BalancedBrackets(expr):
    """
    Check if brackets are balanced in the given expression.
    
    Args:
        expr (str): The expression string to check
        
    Returns:
        bool: True if brackets are balanced, False otherwise
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Set of opening brackets
    opening_brackets = {'(', '{', '['}
    
    # Iterate through each character in the expression
    for char in expr:
        # If it's an opening bracket, push to stack
        if char in opening_brackets:
            stack.append(char)
        # If it's a closing bracket
        elif char in bracket_map:
            # If stack is empty or top doesn't match, brackets are not balanced
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    # If stack is empty, all brackets are balanced
    return len(stack) == 0


# Test cases
if __name__ == "__main__":
    # Test Example 1
    expr1 = "[()]{}{[()()]()}"
    result1 = BalancedBrackets(expr1)
    print(f"Input: {expr1}")
    print(f"Output: {result1}")
    print()
    
    # Test Example 2
    expr2 = "[(])"
    result2 = BalancedBrackets(expr2)
    print(f"Input: {expr2}")
    print(f"Output: {result2}")
    print()
    
    # Additional test cases
    test_cases = [
        "",           # Empty string
        "()",         # Simple balanced
        "()[]{}",     # Multiple types balanced
        "([{}])",     # Nested balanced
        "([)]",       # Nested unbalanced
        "(((",        # Only opening brackets
        ")))",        # Only closing brackets
        "a(b[c]d)e",  # With other characters
    ]
    
    print("Additional test cases:")
    for expr in test_cases:
        result = BalancedBrackets(expr)
        print(f"Input: '{expr}' -> Output: {result}")
