from Node import Node

class SortedNumberList:
    def __init__(self,):
        self.head = None
        self.tail = None    

    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        new_node = Node(number)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        if number <= self.head.get_data():
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node
            return
        if number >= self.tail.get_data():
            new_node.set_previous(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
            return
        current = self.head
        while current is not None and current.get_data() < number:
            current = current.get_next()
         # Insert before current node
        previous_node = current.get_previous()
        new_node.set_next(current)
        new_node.set_previous(previous_node)
        previous_node.set_next(new_node)
        current.set_previous(new_node)


    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        # Case 1: Empty list
        if self.head is None:
            return False
        if self.head.get_data() == number:
            if self.head == self.tail:  # Only one node
                self.head = None
                self.tail = None
            else:  # Multiple nodes
                self.head = self.head.get_next()
                self.head.set_previous(None)
            return True
        if self.tail.get_data() == number:
            self.tail = self.tail.get_previous()
            self.tail.set_next(None)
            return True
        current = self.head
        while current is not None:
            if current.get_data() == number:
                previous_node = current.get_previous()
                next_node = current.get_next()
                previous_node.set_next(next_node)
                if next_node is not None:
                    next_node.set_previous(previous_node)
                return True
            current = current.get_next()
        return False

    # Add any helper methods needed here
