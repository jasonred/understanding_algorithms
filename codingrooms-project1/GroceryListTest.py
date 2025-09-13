from Stack import Stack
from UndoCommand import UndoCommand
from RemoveLastCommand import RemoveLastCommand
from InsertAtCommand import InsertAtCommand
from SwapCommand import SwapCommand
from GroceryList import GroceryList

class GroceryListTest:
    """Stores a list of commands, each of which is one of the five forms:
- add item_name
- removeat index
- swap index1 index2
- undo
- verify list_item1,list_item2,...,last_list_item
"""

    def __init__(self, commands_to_copy):
        self.commands = commands_to_copy[:]
        self.show_commands = True
        self.assert_undo_count = True

    # Compare two lists
    def assert_stack_content(self, actual, expected, test_feedback):
        passed = True

        # First ensure that the sizes match
        if len(actual) != len(expected):
            passed = False

        # Now check compare each item
        if passed:
            for act, exp in zip(actual, expected):
                if act != exp:
                    passed = False

        if not passed:
            print(f"""FAIL:
        Expected items: {expected}
        Actual items:   {actual}""",
                  file=test_feedback,)

        return passed

    def exec_command(self, command, grocery_list, test_feedback):
        # Record the undo stack size prior to executing the command
        undo_count_before = grocery_list.get_undo_stack_size()

        # Store the current undo stack size as the "expected" undo stack size.
        # The expected count is incremented for the add, removeat, and swap
        # commands, and is decremented for the undo command.
        expected_undo_count = grocery_list.get_undo_stack_size()

        # Check the command string
        if command.find("add ") == 0:
            item_to_add = command[4:]
            if self.show_commands:
                print(f"Adding", item_to_add, file=test_feedback,)
                grocery_list.add_with_undo(item_to_add)
                expected_undo_count += 1

        elif command.find("removeat ") == 0:
            index = int(command[9:])
            if self.show_commands:
                print(f"Removing at index", index, file=test_feedback,)
            grocery_list.remove_at_with_undo(index)
            expected_undo_count += 1

        elif command.find("swap ") == 0:
            result, index1, index2 =  self.parse_indices(command[5:])
            if result:
                if self.show_commands:
                    print(f"Swapping at indices", index1, "and", index2, file=test_feedback,)
                grocery_list.swap_with_undo(index1, index2)
            else:
                print("Malformed swap command:", command, file=test_feedback,)
                return False
            expected_undo_count += 1

        elif command == "undo":
            if self.show_commands:
                print(f"Executing undo", file=test_feedback,)
            if 0 == grocery_list.get_undo_stack_size():
                print(f"FAIL: cannot execute undo because undo stack is empty",
                      file=test_feedback,)
            else:
                grocery_list.execute_undo()
            expected_undo_count -= 1

        elif 0 == command.find("verify "):
            list_string = command[7:]
            expected = list_string.split(',')
            actual = grocery_list.get_list_copy()
            if not self.assert_stack_content(actual, expected, test_feedback):
                return False
            print("Verfied list content:", list_string, file=test_feedback,)

        elif command == "verify":
            # Special case for empty list
            actual_size = len(grocery_list.get_list_copy())
            if 0 == actual_size:
                print("PASS: List is empty",  file=test_feedback,)
            else:
                print("FAIL: List should be empty, but instead has ",
                      end='', file=test_feedback,)
                if 1 == actual_size:
                    print("1 item", file=test_feedback,)
                else:
                    print(actual_size, "items", file=test_feedback,)

        if self.assert_undo_count and undo_count_before != expected_undo_count:
            # Get the actual uindo command count
            actual_count = grocery_list.get_undo_stack_size()

            if expected_undo_count != actual_count:
                print(f"""FAIL: Expected undo stack size is {expected_undo_count},
but actual size is {actual_count}""",
                       file=test_feedback,)
                return False
            else:
                print("PASS: Undo stack size is", actual_count, file=test_feedback)

        return True

    def parse_indices(self, str):
        """Attempt to split a string at space and convert to integers"""
        if str.find(" ") < 0:
            return (False, -1, -1)
        num1, num2 = str.split()
        return True, int(num1), int(num2)

    def execute(self, test_feedback):
        self.grocery_list = GroceryList()

        # Execute each command in the command list
        for command in self.commands:
            if not self.exec_command(command, self.grocery_list, test_feedback):
                return False

        # All tests passed
        return True
