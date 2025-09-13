class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class singlyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, val):
        """Add a new node to the end of the list"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, val):
        """Add a new node to the beginning of the list"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def print_list(self):
        """Print the linked list"""
        current = self.head
        values = []
        while current:
            values.append(current.val)
            current = current.next
        print(" -> ".join(map(str, values)) if values else "Empty list")
    
    def reverse_list(self):
        """
        Reverse the direction of the links in the singly linked list
        Returns the new head node
        """
        prev = None
        current = self.head
        
        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the link
            prev = current           # Move prev to current
            current = next_node      # Move current to next
        
        self.head = prev  # Update head to the new first node
        return self.head
    
    def has_cycle(self):
        """
        Check if the linked list contains a cycle using Floyd's cycle detection algorithm
        Returns True if cycle exists, False otherwise
        """
        if not self.head or not self.head.next:
            return False
        
        slow = self.head
        fast = self.head
        
        # Move slow one step and fast two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, there's a cycle
            if slow == fast:
                return True
        
        return False
    
    def has_cycle_with_start_index(self):
        """
        Check if the linked list contains a cycle and return the index where cycle starts
        Returns (True, index) if cycle exists, (False, -1) otherwise
        """
        if not self.head or not self.head.next:
            return False, -1
        
        slow = self.head
        fast = self.head
        
        # Phase 1: Detect if there's a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return False, -1  # No cycle found
        
        # Phase 2: Find the start of the cycle
        slow = self.head
        index = 0
        while slow != fast:
            slow = slow.next
            fast = fast.next
            index += 1
        
        return True, index
