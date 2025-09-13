from Stack import Stack
from InsertAtCommand import InsertAtCommand
from RemoveLastCommand import RemoveLastCommand
from SwapCommand import SwapCommand


class GroceryList:
    def __init__(self):
        self.list_items = []
        self.undo_stack = Stack()

    def add_with_undo(self, new_item_name):
        # Add the list item
        self.list_items.append(new_item_name)

        # Make an undo command that removes the last item and pushes it onto the undo stack
        self.undo_stack.push(RemoveLastCommand(self.list_items))

    def remove_at_with_undo(self, removal_index):
        # Store the item to be removed for undo purposes
        removed_item = self.list_items[removal_index]
        
        # Remove the item at the specified index
        self.list_items.pop(removal_index)
        
        # Create an InsertAtCommand to undo this removal and push it onto the undo stack
        self.undo_stack.push(InsertAtCommand(self.list_items, removal_index, removed_item))

    def swap_with_undo(self, index1, index2):
        # Type your code here.
        # Swap the items at the specified indices
        swap_com = SwapCommand(self.list_items, index1, index2)
        swap_com.execute()
        
        # Create a SwapCommand to undo this swap and push it onto the undo stack
        self.undo_stack.push(SwapCommand(self.list_items, index1, index2))

    def execute_undo(self):
        # Pop the top command from the undo stack and execute it
        command = self.undo_stack.pop()
        command.execute()
        pass

    def get_list_size(self):
       return len(self.list_items)

    def get_undo_stack_size(self):
       return self.undo_stack.size()

    def get_list_copy(self):
       return self.list_items[:]

    def print_list(self, outfil):
        for n, item in enumerate(self.list_items):
            print(f"""{n}. {item}""", file=outfil)
