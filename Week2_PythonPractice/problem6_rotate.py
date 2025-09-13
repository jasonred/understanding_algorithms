"""
Problem 6: Rotate Linked List
You are given the head of a singly linked list and an integer k. Write a 
function rotate that modifies the list so that it is rotated to the right by k positions.
Rotating to the right by one position means that the last node of the list becomes the 
new head, and every other node is shifted one position to the right. When rotating 
by k positions, this process is repeated k times.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate(head, k):
    """
    Rotate the linked list to the right by k positions
    Returns the new head of the rotated list
    
    Args:
        head: Head node of the linked list
        k: Number of positions to rotate right
    
    Returns:
        The new head of the rotated list
    """
    if not head or not head.next or k == 0:
        return head
    
    # Get the length of the list
    length = get_length(head)
    
    # Normalize k to avoid unnecessary rotations
    k = k % length
    
    if k == 0:
        return head
    
    # Find the new tail (length - k - 1) and new head (length - k)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    
    # Find the current tail
    current_tail = new_head
    while current_tail.next:
        current_tail = current_tail.next
    
    # Perform rotation
    new_tail.next = None
    current_tail.next = head
    
    return new_head

def get_length(head):
    """Helper function to get the length of a linked list"""
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

def create_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def print_list(head, name="List"):
    """Helper function to print a linked list"""
    current = head
    values = []
    while current:
        values.append(str(current.val))
        current = current.next
    print(f"{name}: {' -> '.join(values)}")

# Test cases
if __name__ == "__main__":
    print("Testing Rotate Linked List")
    print("=" * 50)
    
    # Test case 1: Example from problem description
    print("Test case 1: 1 -> 2 -> 3 -> 4 -> 5, k = 2")
    head1 = create_list([1, 2, 3, 4, 5])
    print_list(head1, "Original")
    
    rotated1 = rotate(head1, 2)
    print_list(rotated1, "After rotating by 2")
    print("Expected: 4 -> 5 -> 1 -> 2 -> 3")
    print()
    
    # Test case 2: Single rotation
    print("Test case 2: 1 -> 2 -> 3 -> 4 -> 5, k = 1")
    head2 = create_list([1, 2, 3, 4, 5])
    print_list(head2, "Original")
    
    rotated2 = rotate(head2, 1)
    print_list(rotated2, "After rotating by 1")
    print("Expected: 5 -> 1 -> 2 -> 3 -> 4")
    print()
    
    # Test case 3: Rotate by list length (should return original)
    print("Test case 3: 1 -> 2 -> 3, k = 3")
    head3 = create_list([1, 2, 3])
    print_list(head3, "Original")
    
    rotated3 = rotate(head3, 3)
    print_list(rotated3, "After rotating by 3")
    print("Expected: 1 -> 2 -> 3 (same as original)")
    print()
    
    # Test case 4: Rotate by more than list length
    print("Test case 4: 1 -> 2 -> 3, k = 5")
    head4 = create_list([1, 2, 3])
    print_list(head4, "Original")
    
    rotated4 = rotate(head4, 5)
    print_list(rotated4, "After rotating by 5")
    print("Expected: 2 -> 3 -> 1 (k % length = 5 % 3 = 2)")
    print()
    
    # Test case 5: Single node
    print("Test case 5: [1], k = 1")
    head5 = create_list([1])
    print_list(head5, "Original")
    
    rotated5 = rotate(head5, 1)
    print_list(rotated5, "After rotating by 1")
    print("Expected: 1 (single node, no change)")
    print()
    
    # Test case 6: Empty list
    print("Test case 6: [], k = 1")
    head6 = create_list([])
    print_list(head6, "Original")
    
    rotated6 = rotate(head6, 1)
    print_list(rotated6, "After rotating by 1")
    print("Expected: None (empty list)")
    print()
    
    # Test case 7: k = 0
    print("Test case 7: 1 -> 2 -> 3, k = 0")
    head7 = create_list([1, 2, 3])
    print_list(head7, "Original")
    
    rotated7 = rotate(head7, 0)
    print_list(rotated7, "After rotating by 0")
    print("Expected: 1 -> 2 -> 3 (no rotation)")
    print()
    
    # Test case 8: Large k value
    print("Test case 8: 1 -> 2 -> 3 -> 4, k = 6")
    head8 = create_list([1, 2, 3, 4])
    print_list(head8, "Original")
    
    rotated8 = rotate(head8, 6)
    print_list(rotated8, "After rotating by 6")
    print("Expected: 3 -> 4 -> 1 -> 2 (k % length = 6 % 4 = 2)")
