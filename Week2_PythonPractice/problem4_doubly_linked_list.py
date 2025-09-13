"""
Problem 4: Doubly Linked List with Dummy Nodes
Implement a doubly linked list with Dummy Nodes. Create a class 
called doubleLinkedListDummy. Implement the methods provided in the lecture 
notes. Add a method called print, to print the linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class doubleLinkedListDummy:
    def __init__(self):
        # Create dummy head and tail nodes
        self.dummy_head = ListNode(0)  # Dummy head
        self.dummy_tail = ListNode(0)  # Dummy tail
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.size = 0
    
    def append(self, val):
        """Add a new node to the end of the list"""
        new_node = ListNode(val)
        
        # Insert before dummy tail
        new_node.next = self.dummy_tail
        new_node.prev = self.dummy_tail.prev
        self.dummy_tail.prev.next = new_node
        self.dummy_tail.prev = new_node
        
        self.size += 1
    
    def prepend(self, val):
        """Add a new node to the beginning of the list"""
        new_node = ListNode(val)
        
        # Insert after dummy head
        new_node.prev = self.dummy_head
        new_node.next = self.dummy_head.next
        self.dummy_head.next.prev = new_node
        self.dummy_head.next = new_node
        
        self.size += 1
    
    def remove(self, val):
        """Remove the first occurrence of val from the list"""
        current = self.dummy_head.next
        
        while current != self.dummy_tail:
            if current.val == val:
                # Remove the node
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def print(self):
        """Print the doubly linked list"""
        current = self.dummy_head.next
        values = []
        
        while current != self.dummy_tail:
            values.append(current.val)
            current = current.next
        
        print(" <-> ".join(map(str, values)) if values else "Empty list")
    
    def print_reverse(self):
        """Print the doubly linked list in reverse order"""
        current = self.dummy_tail.prev
        values = []
        
        while current != self.dummy_head:
            values.append(current.val)
            current = current.prev
        
        print(" <-> ".join(map(str, values)) if values else "Empty list")
    
    def get_size(self):
        """Return the size of the list"""
        return self.size
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.size == 0
    
    def find(self, val):
        """Find the first occurrence of val in the list"""
        current = self.dummy_head.next
        index = 0
        
        while current != self.dummy_tail:
            if current.val == val:
                return index
            current = current.next
            index += 1
        
        return -1


# Test cases
if __name__ == "__main__":
    print("Testing Doubly Linked List with Dummy Nodes")
    print("=" * 50)
    
    # Create a new doubly linked list
    dll = doubleLinkedListDummy()
    
    # Test append
    print("1. Testing append:")
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.print()
    print(f"Size: {dll.get_size()}")
    print()
    
    # Test prepend
    print("2. Testing prepend:")
    dll.prepend(0)
    dll.print()
    print(f"Size: {dll.get_size()}")
    print()
    
    # Test print_reverse
    print("3. Testing reverse print:")
    dll.print_reverse()
    print()
    
    # Test find
    print("4. Testing find:")
    print(f"Find 2: index {dll.find(2)}")
    print(f"Find 5: index {dll.find(5)}")
    print()
    
    # Test remove
    print("5. Testing remove:")
    print("Before removing 2:")
    dll.print()
    dll.remove(2)
    print("After removing 2:")
    dll.print()
    print(f"Size: {dll.get_size()}")
    print()
    
    # Test remove non-existent
    print("6. Testing remove non-existent element:")
    result = dll.remove(99)
    print(f"Remove 99: {result}")
    dll.print()
    print()
    
    # Test empty list
    print("7. Testing empty list operations:")
    empty_dll = doubleLinkedListDummy()
    print("Empty list:")
    empty_dll.print()
    print(f"Is empty: {empty_dll.is_empty()}")
    print(f"Size: {empty_dll.get_size()}")
    print(f"Find 1: {empty_dll.find(1)}")
    print(f"Remove 1: {empty_dll.remove(1)}")
