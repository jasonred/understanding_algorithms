class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    """
    Determine if a singly linked list is a palindrome.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        head: The head of the linked list
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    if not head or not head.next:
        return True
    
    # Step 1: Find the middle of the list using fast/slow pointers
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half of the list
    second_half = reverse_list(slow)
    
    # Step 3: Compare the first half with the reversed second half
    first_half = head
    is_palindrome = True
    
    while second_half and is_palindrome:
        if first_half.val != second_half.val:
            is_palindrome = False
        first_half = first_half.next
        second_half = second_half.next
    
    # Step 4: Restore the original list (optional but good practice)
    reverse_list(slow)
    
    return is_palindrome

def reverse_list(head: ListNode) -> ListNode:
    """
    Reverse a linked list in-place.
    
    Args:
        head: The head of the list to reverse
        
    Returns:
        ListNode: The new head of the reversed list
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

# Test cases
def create_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def print_list(head):
    """Helper function to print a linked list."""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

# Test the implementation
if __name__ == "__main__":
    # Test case 1: [1, 2, 2, 1] - should be True
    test1 = create_list([1, 2, 2, 1])
    print(f"Test 1: {print_list(test1)} -> {isPalindrome(test1)}")
    
    # Test case 2: [1, 2] - should be False
    test2 = create_list([1, 2])
    print(f"Test 2: {print_list(test2)} -> {isPalindrome(test2)}")
    
    # Test case 3: [1, 2, 3, 2, 1] - should be True
    test3 = create_list([1, 2, 3, 2, 1])
    print(f"Test 3: {print_list(test3)} -> {isPalindrome(test3)}")
    
    # Test case 4: [1] - should be True
    test4 = create_list([1])
    print(f"Test 4: {print_list(test4)} -> {isPalindrome(test4)}")
    
    # Test case 5: [] - should be True
    test5 = create_list([])
    print(f"Test 5: {print_list(test5)} -> {isPalindrome(test5)}")
    
    # Test case 6: [1, 2, 3, 4, 5] - should be False
    test6 = create_list([1, 2, 3, 4, 5])
    print(f"Test 6: {print_list(test6)} -> {isPalindrome(test6)}")
