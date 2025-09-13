class Queue:
    def __init__(self, maxsize=5):
        """
        Initialize a Queue using two stacks.
        
        Args:
            maxsize (int): Maximum number of elements the queue can hold (default: 5)
        """
        self.maxsize = maxsize
        self.stack1 = []  # Used for enqueue operations
        self.stack2 = []  # Used for dequeue operations
    
    def enqueue(self, value):
        """
        Add a new item to the queue.
        
        Args:
            value: The item to add to the queue
            
        Raises:
            OverflowError: If the queue is full (reached maxsize)
        """
        # Check if queue is full
        if len(self.stack1) + len(self.stack2) >= self.maxsize:
            raise OverflowError("Queue is full")
        
        # Simply push to stack1 for enqueue
        self.stack1.append(value)
    
    def dequeue(self):
        """
        Remove and return the oldest item from the queue.
        
        Returns:
            The oldest item in the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        # If both stacks are empty, queue is empty
        if not self.stack1 and not self.stack2:
            raise IndexError("Queue is empty")
        
        # If stack2 is empty, transfer all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Pop from stack2 (this gives us the oldest element)
        return self.stack2.pop()
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
    def is_full(self):
        """
        Check if the queue is full.
        
        Returns:
            bool: True if queue is full, False otherwise
        """
        return len(self.stack1) + len(self.stack2) >= self.maxsize
    
    def size(self):
        """
        Get the current number of elements in the queue.
        
        Returns:
            int: Number of elements in the queue
        """
        return len(self.stack1) + len(self.stack2)
    
    def __str__(self):
        """
        String representation of the queue.
        
        Returns:
            str: String representation showing both stacks
        """
        # Create a list representing the queue order
        queue_list = []
        
        # Add elements from stack2 (in reverse order since we want oldest first)
        for i in range(len(self.stack2) - 1, -1, -1):
            queue_list.append(self.stack2[i])
        
        # Add elements from stack1 (in order)
        queue_list.extend(self.stack1)
        
        return f"Queue({queue_list})"


# Test cases
if __name__ == "__main__":
    print("Testing Queue with two stacks:")
    print("=" * 40)
    
    # Test 1: Basic enqueue and dequeue
    print("\nTest 1: Basic operations")
    q = Queue(maxsize=5)
    print(f"Initial queue: {q}")
    print(f"Is empty: {q.is_empty()}")
    
    # Enqueue some elements
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"After enqueue(1,2,3): {q}")
    print(f"Size: {q.size()}")
    
    # Dequeue elements
    print(f"Dequeue: {q.dequeue()}")  # Should return 1
    print(f"After dequeue: {q}")
    print(f"Dequeue: {q.dequeue()}")  # Should return 2
    print(f"After dequeue: {q}")
    
    # Test 2: FIFO behavior
    print("\nTest 2: FIFO behavior verification")
    q2 = Queue(maxsize=10)
    for i in range(5):
        q2.enqueue(f"item_{i}")
    print(f"Queue after adding 5 items: {q2}")
    
    print("Dequeuing all items:")
    for i in range(5):
        item = q2.dequeue()
        print(f"  Dequeued: {item}")
    print(f"Final queue: {q2}")
    print(f"Is empty: {q2.is_empty()}")
    
    # Test 3: Mixed enqueue/dequeue operations
    print("\nTest 3: Mixed operations")
    q3 = Queue(maxsize=5)
    q3.enqueue('A')
    q3.enqueue('B')
    print(f"After enqueue A, B: {q3}")
    
    print(f"Dequeue: {q3.dequeue()}")  # Should return 'A'
    print(f"After dequeue: {q3}")
    
    q3.enqueue('C')
    q3.enqueue('D')
    print(f"After enqueue C, D: {q3}")
    
    print(f"Dequeue: {q3.dequeue()}")  # Should return 'B'
    print(f"Dequeue: {q3.dequeue()}")  # Should return 'C'
    print(f"Final: {q3}")
    
    # Test 4: Error handling
    print("\nTest 4: Error handling")
    q4 = Queue(maxsize=3)
    
    # Fill the queue
    for i in range(3):
        q4.enqueue(i)
    print(f"Full queue: {q4}")
    print(f"Is full: {q4.is_full()}")
    
    # Try to enqueue when full
    try:
        q4.enqueue(99)
    except OverflowError as e:
        print(f"Expected error when enqueueing to full queue: {e}")
    
    # Empty the queue
    for i in range(3):
        q4.dequeue()
    print(f"Empty queue: {q4}")
    print(f"Is empty: {q4.is_empty()}")
    
    # Try to dequeue when empty
    try:
        q4.dequeue()
    except IndexError as e:
        print(f"Expected error when dequeuing from empty queue: {e}")
    
    # Test 5: Performance test with larger queue
    print("\nTest 5: Performance test")
    q5 = Queue(maxsize=1000)
    
    # Add many items
    for i in range(100):
        q5.enqueue(i)
    print(f"Added 100 items, size: {q5.size()}")
    
    # Remove some items
    for i in range(50):
        q5.dequeue()
    print(f"Removed 50 items, size: {q5.size()}")
    
    # Add more items
    for i in range(100, 150):
        q5.enqueue(i)
    print(f"Added 50 more items, size: {q5.size()}")
    
    # Verify FIFO order
    print("First 5 dequeued items:")
    for i in range(5):
        print(f"  {q5.dequeue()}")
