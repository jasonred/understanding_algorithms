#!/usr/bin/env python3

from GroceryList import GroceryList
import sys

def test_undo():
    print("Testing execute_undo method...")
    
    # Create a grocery list
    grocery_list = GroceryList()
    
    # Add some items
    print("Adding 'apple'...")
    grocery_list.add_with_undo("apple")
    print(f"List size: {grocery_list.get_list_size()}")
    print(f"Undo stack size: {grocery_list.get_undo_stack_size()}")
    print(f"List: {grocery_list.get_list_copy()}")
    
    print("\nAdding 'banana'...")
    grocery_list.add_with_undo("banana")
    print(f"List size: {grocery_list.get_list_size()}")
    print(f"Undo stack size: {grocery_list.get_undo_stack_size()}")
    print(f"List: {grocery_list.get_list_copy()}")
    
    # Test undo
    print("\nExecuting undo...")
    grocery_list.execute_undo()
    print(f"List size: {grocery_list.get_list_size()}")
    print(f"Undo stack size: {grocery_list.get_undo_stack_size()}")
    print(f"List: {grocery_list.get_list_copy()}")
    
    # Test another undo
    print("\nExecuting another undo...")
    grocery_list.execute_undo()
    print(f"List size: {grocery_list.get_list_size()}")
    print(f"Undo stack size: {grocery_list.get_undo_stack_size()}")
    print(f"List: {grocery_list.get_list_copy()}")
    
    # Test undo on empty stack
    print("\nTesting undo on empty stack...")
    grocery_list.execute_undo()
    print(f"List size: {grocery_list.get_list_size()}")
    print(f"Undo stack size: {grocery_list.get_undo_stack_size()}")
    print(f"List: {grocery_list.get_list_copy()}")

if __name__ == "__main__":
    test_undo()
