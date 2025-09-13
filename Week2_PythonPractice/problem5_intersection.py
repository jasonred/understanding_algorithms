"""
Problem 5: Intersection of Two Linked Lists
Given the heads of two singly linked-lists headA and headB, return the 
node at which the two lists intersect. If the two linked lists have no intersection at 
all, return null.

For example, the following two linked lists begin to intersect at node c1:
Assume that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    """
    Find the intersection node of two singly linked lists
    Returns the intersection node if exists, None otherwise
    
    Args:
        headA: Head node of first linked list
        headB: Head node of second linked list
    
    Returns:
        The intersection node if exists, None otherwise
    """
    if not headA or not headB:
        return None
    
    # Get lengths of both lists
    lenA = get_length(headA)
    lenB = get_length(headB)
    
    # Move the longer list's head to align the lists
    if lenA > lenB:
        for _ in range(lenA - lenB):
            headA = headA.next
    else:
        for _ in range(lenB - lenA):
            headB = headB.next
    
    # Now both lists are aligned, find intersection
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    
    return None

def get_length(head):
    """Helper function to get the length of a linked list"""
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

def create_intersecting_lists():
    """
    Helper function to create two intersecting linked lists for testing
    Returns (headA, headB, expected_intersection_value)
    """
    # Create intersection node
    intersection = ListNode(3)
    intersection.next = ListNode(4)
    intersection.next.next = ListNode(5)
    
    # Create list A: 1 -> 2 -> 3 -> 4 -> 5
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = intersection
    
    # Create list B: 6 -> 7 -> 3 -> 4 -> 5 (intersects at node with value 3)
    headB = ListNode(6)
    headB.next = ListNode(7)
    headB.next.next = intersection
    
    return headA, headB, 3

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
    print("Testing Intersection of Two Linked Lists")
    print("=" * 50)
    
    # Test case 1: Intersecting lists
    print("Test case 1: Intersecting lists")
    headA, headB, expected_val = create_intersecting_lists()
    
    print_list(headA, "List A")
    print_list(headB, "List B")
    
    result = getIntersectionNode(headA, headB)
    if result:
        print(f"Intersection found at node with value: {result.val}")
        print(f"Expected value: {expected_val}")
        print(f"Test passed: {result.val == expected_val}")
    else:
        print("No intersection found")
    print()
    
    # Test case 2: Non-intersecting lists
    print("Test case 2: Non-intersecting lists")
    headA2 = ListNode(1)
    headA2.next = ListNode(2)
    headA2.next.next = ListNode(3)
    
    headB2 = ListNode(4)
    headB2.next = ListNode(5)
    headB2.next.next = ListNode(6)
    
    print_list(headA2, "List A")
    print_list(headB2, "List B")
    
    result2 = getIntersectionNode(headA2, headB2)
    if result2:
        print(f"Intersection found at node with value: {result2.val}")
    else:
        print("No intersection found (expected)")
    print()
    
    # Test case 3: One empty list
    print("Test case 3: One empty list")
    headA3 = ListNode(1)
    headA3.next = ListNode(2)
    headB3 = None
    
    print_list(headA3, "List A")
    print("List B: None")
    
    result3 = getIntersectionNode(headA3, headB3)
    if result3:
        print(f"Intersection found at node with value: {result3.val}")
    else:
        print("No intersection found (expected)")
    print()
    
    # Test case 4: Both empty lists
    print("Test case 4: Both empty lists")
    result4 = getIntersectionNode(None, None)
    if result4:
        print(f"Intersection found at node with value: {result4.val}")
    else:
        print("No intersection found (expected)")
    print()
    
    # Test case 5: Same length intersecting lists
    print("Test case 5: Same length intersecting lists")
    intersection5 = ListNode(10)
    intersection5.next = ListNode(11)
    
    headA5 = ListNode(1)
    headA5.next = ListNode(2)
    headA5.next.next = intersection5
    
    headB5 = ListNode(3)
    headB5.next = ListNode(4)
    headB5.next.next = intersection5
    
    print_list(headA5, "List A")
    print_list(headB5, "List B")
    
    result5 = getIntersectionNode(headA5, headB5)
    if result5:
        print(f"Intersection found at node with value: {result5.val}")
        print(f"Test passed: {result5.val == 10}")
    else:
        print("No intersection found")
