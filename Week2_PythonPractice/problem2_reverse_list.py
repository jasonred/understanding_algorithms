"""
Problem 2: Reverse Linked List
Write a python function reverse_list(linkedList) that reverses the 
direction of the links in a singly linked list passed as parameter and returns the head 
node. Add this method to the singlyLinkedList class. Check singlyLinkedList.py. 
Hint: Think about how you can change the direction of the links in the list without 
losing track of where you are. You need to reverse the direction of the next pointers. 
To do this, keep track of three pointers: the current node you are processing, the 
previous node, and the next node. By iterating through the list and updating the next 
pointer of each node to point to the previous node, you effectively reverse the list.
"""

from singlyLinkedList import singlyLinkedList

def reverse_list(linkedList):
    """
    Reverse the direction of the links in a singly linked list
    Returns the new head node
    
    Args:
        linkedList: singlyLinkedList object to reverse
    
    Returns:
        The new head node of the reversed list
    """
    prev = None
    current = linkedList.head
    
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        prev = current           # Move prev to current
        current = next_node      # Move current to next
    
    linkedList.head = prev  # Update head to the new first node
    return linkedList.head


# Test cases
if __name__ == "__main__":
    # Test case 1: 1 -> 2 -> 3
    print("Test case 1:")
    ll = singlyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    print("Original list:")
    ll.print_list()
    
    # Reverse the list
    reverse_list(ll)
    print("Reversed list:")
    ll.print_list()
    print()
    
    # Test case 2: Single node
    print("Test case 2 (single node):")
    ll2 = singlyLinkedList()
    ll2.append(42)
    
    print("Original list:")
    ll2.print_list()
    
    reverse_list(ll2)
    print("Reversed list:")
    ll2.print_list()
    print()
    
    # Test case 3: Empty list
    print("Test case 3 (empty list):")
    ll3 = singlyLinkedList()
    
    print("Original list:")
    ll3.print_list()
    
    reverse_list(ll3)
    print("Reversed list:")
    ll3.print_list()
