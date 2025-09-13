"""
Problem 3: Has Cycle in Linked List
Write a python function has_cycle that returns True if the linked list 
passed as parameter contains a cycle. Otherwise returns False.
Add this method to the singlyLinkedList class. Check singlyLinkedList.py.
Hint: There is a cycle in a linked list if at least one node in the list that can be visited 
again by following the next pointer.
"""

from singlyLinkedList import singlyLinkedList

def has_cycle(linkedList):
    """
    Check if the linked list contains a cycle using Floyd's cycle detection algorithm
    Returns True if cycle exists, False otherwise
    
    Args:
        linkedList: singlyLinkedList object to check for cycles
    
    Returns:
        True if cycle exists, False otherwise
    """
    if not linkedList.head or not linkedList.head.next:
        return False
    
    slow = linkedList.head
    fast = linkedList.head
    
    # Move slow one step and fast two steps
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # If they meet, there's a cycle
        if slow == fast:
            return True
    
    return False


def has_cycle_with_start_index(linkedList):
    """
    Check if the linked list contains a cycle and return the index where cycle starts
    Returns (True, index) if cycle exists, (False, -1) otherwise
    
    Args:
        linkedList: singlyLinkedList object to check for cycles
    
    Returns:
        Tuple of (has_cycle, start_index)
    """
    if not linkedList.head or not linkedList.head.next:
        return False, -1
    
    slow = linkedList.head
    fast = linkedList.head
    
    # Phase 1: Detect if there's a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return False, -1  # No cycle found
    
    # Phase 2: Find the start of the cycle
    slow = linkedList.head
    index = 0
    while slow != fast:
        slow = slow.next
        fast = fast.next
        index += 1
    
    return True, index


# Test cases
if __name__ == "__main__":
    # Test case 1: List without cycle
    print("Test case 1 (no cycle):")
    ll1 = singlyLinkedList()
    ll1.append(1)
    ll1.append(2)
    ll1.append(3)
    ll1.append(4)
    
    print("List:")
    ll1.print_list()
    print(f"Has cycle: {has_cycle(ll1)}")
    print()
    
    # Test case 2: List with cycle (create manually)
    print("Test case 2 (with cycle):")
    ll2 = singlyLinkedList()
    ll2.append(1)
    ll2.append(2)
    ll2.append(3)
    ll2.append(4)
    
    # Create a cycle: 4 -> 2
    ll2.head.next.next.next.next = ll2.head.next
    
    print("List with cycle: 1 -> 2 -> 3 -> 4 -> 2 (cycle)")
    print(f"Has cycle: {has_cycle(ll2)}")
    
    # Test cycle start index
    has_cycle_result, start_index = has_cycle_with_start_index(ll2)
    print(f"Cycle starts at index: {start_index}")
    print()
    
    # Test case 3: Single node (no cycle)
    print("Test case 3 (single node):")
    ll3 = singlyLinkedList()
    ll3.append(1)
    
    print("List:")
    ll3.print_list()
    print(f"Has cycle: {has_cycle(ll3)}")
    print()
    
    # Test case 4: Empty list
    print("Test case 4 (empty list):")
    ll4 = singlyLinkedList()
    
    print("List:")
    ll4.print_list()
    print(f"Has cycle: {has_cycle(ll4)}")
