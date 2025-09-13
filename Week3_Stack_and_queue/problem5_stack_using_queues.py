class Stack:
    def __init__(self, maxsize=5):
        """
        Initialize a Stack using one queue.
        
        Args:
            maxsize (int): Maximum number of elements the stack can hold (default: 5)
        """
        self.maxsize = maxsize
        self.queue = []  # Using Python list as queue (append for enqueue, pop(0) for dequeue)
    
    def push(self, value):
        """
        Add a new item to the stack.
        
        Args:
            value: The item to add to the stack
            
        Raises:
            OverflowError: If the stack is full (reached maxsize)
        """
        # Check if stack is full
        if len(self.queue) >= self.maxsize:
            raise OverflowError("Stack is full")
        
        # Add the new element to the queue
        self.queue.append(value)
        
        # Rotate the queue to make the new element the first one
        # This ensures LIFO behavior (Last In, First Out)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
    
    def pop(self):
        """
        Remove and return the most recently added item from the stack.
        
        Returns:
            The most recently added item in the stack
            
        Raises:
            IndexError: If the stack is empty
        """
        if not self.queue:
            raise IndexError("Stack is empty")
        
        # Since we rotated during push, the first element is the most recent
        return self.queue.pop(0)
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
        """
        return len(self.queue) == 0
    
    def is_full(self):
        """
        Check if the stack is full.
        
        Returns:
            bool: True if stack is full, False otherwise
        """
        return len(self.queue) >= self.maxsize
    
    def size(self):
        """
        Get the current number of elements in the stack.
        
        Returns:
            int: Number of elements in the stack
        """
        return len(self.queue)
    
    def peek(self):
        """
        Get the top element without removing it.
        
        Returns:
            The top element of the stack
            
        Raises:
            IndexError: If the stack is empty
        """
        if not self.queue:
            raise IndexError("Stack is empty")
        
        return self.queue[0]
    
    def __str__(self):
        """
        String representation of the stack.
        
        Returns:
            str: String representation showing stack from top to bottom
        """
        return f"Stack({self.queue})"


class StackTwoQueues:
    def __init__(self, maxsize=5):
        """
        Initialize a Stack using two queues.
        
        Args:
            maxsize (int): Maximum number of elements the stack can hold (default: 5)
        """
        self.maxsize = maxsize
        self.queue1 = []  # Primary queue
        self.queue2 = []  # Helper queue
    
    def push(self, value):
        """
        Add a new item to the stack.
        
        Args:
            value: The item to add to the stack
            
        Raises:
            OverflowError: If the stack is full (reached maxsize)
        """
        # Check if stack is full
        if len(self.queue1) + len(self.queue2) >= self.maxsize:
            raise OverflowError("Stack is full")
        
        # Add the new element to queue1
        self.queue1.append(value)
    
    def pop(self):
        """
        Remove and return the most recently added item from the stack.
        
        Returns:
            The most recently added item in the stack
            
        Raises:
            IndexError: If the stack is empty
        """
        if not self.queue1 and not self.queue2:
            raise IndexError("Stack is empty")
        
        # Move all elements except the last one from queue1 to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        # The last element in queue1 is our target
        result = self.queue1.pop(0)
        
        # Swap the queues so queue2 becomes the primary queue
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return result
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
        """
        return len(self.queue1) == 0 and len(self.queue2) == 0
    
    def is_full(self):
        """
        Check if the stack is full.
        
        Returns:
            bool: True if stack is full, False otherwise
        """
        return len(self.queue1) + len(self.queue2) >= self.maxsize
    
    def size(self):
        """
        Get the current number of elements in the stack.
        
        Returns:
            int: Number of elements in the stack
        """
        return len(self.queue1) + len(self.queue2)
    
    def peek(self):
        """
        Get the top element without removing it.
        
        Returns:
            The top element of the stack
            
        Raises:
            IndexError: If the stack is empty
        """
        if not self.queue1 and not self.queue2:
            raise IndexError("Stack is empty")
        
        # Move all elements except the last one from queue1 to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        # The last element in queue1 is our target
        result = self.queue1[0]
        
        # Move the last element to queue2 as well
        self.queue2.append(self.queue1.pop(0))
        
        # Swap the queues so queue2 becomes the primary queue
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return result
    
    def __str__(self):
        """
        String representation of the stack.
        
        Returns:
            str: String representation showing stack from top to bottom
        """
        # Create a list representing the stack order
        stack_list = []
        
        # Add elements from queue1 (in order)
        stack_list.extend(self.queue1)
        
        # Add elements from queue2 (in order)
        stack_list.extend(self.queue2)
        
        return f"StackTwoQueues({stack_list})"


# Test cases
if __name__ == "__main__":
    print("Testing Stack with one queue:")
    print("=" * 40)
    
    # Test 1: Basic push and pop
    print("\nTest 1: Basic operations")
    s = Stack(maxsize=5)
    print(f"Initial stack: {s}")
    print(f"Is empty: {s.is_empty()}")
    
    # Push some elements
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"After push(1,2,3): {s}")
    print(f"Size: {s.size()}")
    print(f"Peek: {s.peek()}")
    
    # Pop elements
    print(f"Pop: {s.pop()}")  # Should return 3
    print(f"After pop: {s}")
    print(f"Pop: {s.pop()}")  # Should return 2
    print(f"After pop: {s}")
    
    # Test 2: LIFO behavior
    print("\nTest 2: LIFO behavior verification")
    s2 = Stack(maxsize=10)
    for i in range(5):
        s2.push(f"item_{i}")
    print(f"Stack after adding 5 items: {s2}")
    
    print("Popping all items:")
    for i in range(5):
        item = s2.pop()
        print(f"  Popped: {item}")
    print(f"Final stack: {s2}")
    print(f"Is empty: {s2.is_empty()}")
    
    # Test 3: Mixed push/pop operations
    print("\nTest 3: Mixed operations")
    s3 = Stack(maxsize=5)
    s3.push('A')
    s3.push('B')
    print(f"After push A, B: {s3}")
    
    print(f"Pop: {s3.pop()}")  # Should return 'B'
    print(f"After pop: {s3}")
    
    s3.push('C')
    s3.push('D')
    print(f"After push C, D: {s3}")
    
    print(f"Pop: {s3.pop()}")  # Should return 'D'
    print(f"Pop: {s3.pop()}")  # Should return 'C'
    print(f"Final: {s3}")
    
    # Test 4: Error handling
    print("\nTest 4: Error handling")
    s4 = Stack(maxsize=3)
    
    # Fill the stack
    for i in range(3):
        s4.push(i)
    print(f"Full stack: {s4}")
    print(f"Is full: {s4.is_full()}")
    
    # Try to push when full
    try:
        s4.push(99)
    except OverflowError as e:
        print(f"Expected error when pushing to full stack: {e}")
    
    # Empty the stack
    for i in range(3):
        s4.pop()
    print(f"Empty stack: {s4}")
    print(f"Is empty: {s4.is_empty()}")
    
    # Try to pop when empty
    try:
        s4.pop()
    except IndexError as e:
        print(f"Expected error when popping from empty stack: {e}")
    
    print("\n" + "=" * 50)
    print("Testing Stack with two queues:")
    print("=" * 50)
    
    # Test 1: Basic push and pop with two queues
    print("\nTest 1: Basic operations")
    s2q = StackTwoQueues(maxsize=5)
    print(f"Initial stack: {s2q}")
    print(f"Is empty: {s2q.is_empty()}")
    
    # Push some elements
    s2q.push(1)
    s2q.push(2)
    s2q.push(3)
    print(f"After push(1,2,3): {s2q}")
    print(f"Size: {s2q.size()}")
    print(f"Peek: {s2q.peek()}")
    
    # Pop elements
    print(f"Pop: {s2q.pop()}")  # Should return 3
    print(f"After pop: {s2q}")
    print(f"Pop: {s2q.pop()}")  # Should return 2
    print(f"After pop: {s2q}")
    
    # Test 2: LIFO behavior with two queues
    print("\nTest 2: LIFO behavior verification")
    s2q2 = StackTwoQueues(maxsize=10)
    for i in range(5):
        s2q2.push(f"item_{i}")
    print(f"Stack after adding 5 items: {s2q2}")
    
    print("Popping all items:")
    for i in range(5):
        item = s2q2.pop()
        print(f"  Popped: {item}")
    print(f"Final stack: {s2q2}")
    print(f"Is empty: {s2q2.is_empty()}")
    
    # Test 3: Performance comparison
    print("\nTest 3: Performance comparison")
    import time
    
    # Test single queue implementation
    start_time = time.time()
    s_perf1 = Stack(maxsize=1000)
    for i in range(100):
        s_perf1.push(i)
    for i in range(100):
        s_perf1.pop()
    single_queue_time = time.time() - start_time
    
    # Test two queue implementation
    start_time = time.time()
    s_perf2 = StackTwoQueues(maxsize=1000)
    for i in range(100):
        s_perf2.push(i)
    for i in range(100):
        s_perf2.pop()
    two_queue_time = time.time() - start_time
    
    print(f"Single queue implementation time: {single_queue_time:.6f} seconds")
    print(f"Two queue implementation time: {two_queue_time:.6f} seconds")
    print(f"Performance difference: {abs(single_queue_time - two_queue_time):.6f} seconds")
