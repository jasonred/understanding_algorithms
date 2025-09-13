def PostfixEval(expr):
    """
    Evaluate a mathematical expression in postfix notation (Reverse Polish Notation).
    
    Args:
        expr (list): List of strings containing operands and operators
        
    Returns:
        float: Result of the postfix expression
        
    Raises:
        ValueError: If the expression is invalid (insufficient operands, invalid operators)
    """
    if not expr:
        raise ValueError("Empty expression")
    
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in expr:
        # Remove any whitespace from token
        token = token.strip()
        
        if token in operators:
            # It's an operator - need at least 2 operands on stack
            if len(stack) < 2:
                raise ValueError(f"Insufficient operands for operator '{token}'")
            
            # Pop the two most recent operands
            b = stack.pop()  # Second operand (right side)
            a = stack.pop()  # First operand (left side)
            
            # Perform the operation
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            
            # Push result back onto stack
            stack.append(result)
        else:
            # It's an operand - convert to float and push onto stack
            try:
                operand = float(token)
                stack.append(operand)
            except ValueError:
                raise ValueError(f"Invalid operand: '{token}'")
    
    # After processing all tokens, stack should have exactly one element
    if len(stack) != 1:
        raise ValueError("Invalid expression: too many operands or insufficient operators")
    
    return stack[0]


# Test cases
if __name__ == "__main__":
    # Test Example 1
    expr1 = ['3', '4', '+', '2', '*', '7', '/']
    result1 = PostfixEval(expr1)
    print(f"Input: {expr1}")
    print(f"Output: {result1}")
    print()
    
    # Additional test cases
    test_cases = [
        # Basic operations
        (['2', '3', '+'], 5.0),           # 2 + 3 = 5
        (['10', '5', '-'], 5.0),          # 10 - 5 = 5
        (['4', '5', '*'], 20.0),          # 4 * 5 = 20
        (['15', '3', '/'], 5.0),          # 15 / 3 = 5
        
        # Complex expressions
        (['3', '4', '+', '2', '*'], 14.0),  # (3 + 4) * 2 = 14
        (['5', '1', '2', '+', '4', '*', '+', '3', '-'], 14.0),  # 5 + (1 + 2) * 4 - 3 = 14
        (['2', '3', '4', '+', '*'], 14.0),  # 2 * (3 + 4) = 14
        
        # Decimal numbers
        (['3.5', '2.5', '+'], 6.0),       # 3.5 + 2.5 = 6.0
        (['10.0', '3.0', '/'], 3.3333333333333335),  # 10 / 3 ≈ 3.33...
        
        # Single number
        (['42'], 42.0),                   # Just a number
    ]
    
    print("Additional test cases:")
    for expr, expected in test_cases:
        try:
            result = PostfixEval(expr)
            status = "✓" if abs(result - expected) < 1e-10 else "✗"
            print(f"{status} Input: {expr} -> Output: {result} (Expected: {expected})")
        except Exception as e:
            print(f"✗ Input: {expr} -> Error: {e}")
    
    # Error cases
    print("\nError cases:")
    error_cases = [
        ['+'],                    # Insufficient operands
        ['2', '+'],              # Insufficient operands
        ['2', '3', '4', '+'],    # Too many operands
        ['2', '3', 'unknown'],   # Invalid operator
        ['2', '3', '+', '0', '/'],  # Division by zero
        [],                      # Empty expression
    ]
    
    for expr in error_cases:
        try:
            result = PostfixEval(expr)
            print(f"✗ Input: {expr} -> Unexpected success: {result}")
        except Exception as e:
            print(f"✓ Input: {expr} -> Expected error: {e}")
    
    # Trace through Example 1
    print(f"\nTracing Example 1: {expr1}")
    print("Step by step evaluation:")
    stack = []
    for i, token in enumerate(expr1):
        token = token.strip()
        if token in {'+', '-', '*', '/'}:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            print(f"  Step {i+1}: {a} {token} {b} = {result}")
            stack.append(result)
        else:
            stack.append(float(token))
            print(f"  Step {i+1}: Push {token} -> Stack: {stack}")
    print(f"Final result: {stack[0]}")
