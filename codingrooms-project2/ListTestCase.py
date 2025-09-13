from SortedNumberList import SortedNumberList

# ListOp represents either an insertion or removal operation for a test case.
class ListOp:
    def __init__(self,
               is_op_insertion,
               number_value,
               expected_list_content,
               expected_ret_val = False):
        self.is_insertion = is_op_insertion   # True for insertion, False for removal
        self.number = number_value
        self.expected_list = expected_list_content
        self.return_value = expected_ret_val

# ListTestCase stores an ordered collection of ListOp objects, representing
# operations for the test case. The test case is executed by calling
# ListTestCase's Execute() member function.
class ListTestCase:
    def __init__(self, operations_to_copy):
        self.operations = operations_to_copy

    # Executes the test case, writing feedback to the test_feedback stream. True
    # is returned if the test case passes, False is returned if the test case
    # fails.
    def execute(self, outfil):
        # Create an instance of the user's SortedNumberList
        num_list = SortedNumberList()

        for test_case_op in self.operations:
            # Perform either the insertion or removal
            if test_case_op.is_insertion:
                num_list.insert(test_case_op.number)
            else:
                actual_return_value = num_list.remove(test_case_op.number)

                # Verify that return value is correct
                if actual_return_value != test_case_op.return_value:
                    print(f"""FAIL: remove({test_case_op.number}) returned {'True' if actual_return_value else 'False'},""",
                          file=outfil,)
                    print(f"""but should have returned {'True' if test_case_op.return_value else 'False'}.""",
                          file=outfil,)
                    return False

            # Check list for a circular reference first. A circular reference
            # results in an infnite loop in the subsequent list verification, so
            # the check for a circular reference must occur prior.
            encountered_nodes = set()
            user_node = num_list.head
            while user_node:
                # A node linking to itself merits a special-case failure message
                if user_node == user_node.get_next():
                    print(f"""FAIL: node with data {user_node.get_data()} has a next pointer pointing to itself.""",
                          file=outfil,)
                    return False

                # Check if the node was previously encountered
                if user_node in encountered_nodes:
                    print(f"""FAIL: node with data {user_node.get_data()} was encountered more than once when iterating""",
                          file=outfil,)
                    print(f"""through the list. so the list has a circular reference.""",
                          file=outfil)
                    return False

                # Add the node to the set
                encountered_nodes.add(user_node)

                # Advance to the next node
                user_node = user_node.get_next()

            # Verify list content
            user_node = num_list.head
            index = 0
            for expected_num in test_case_op.expected_list:
                # If the node is null or the node's number doesn't match the
                # expected, then the test has failed
                if not user_node or user_node.get_data() != expected_num:
                    print(f"""FAIL: {'Insert' if test_case_op.is_insertion else 'Remove'}  {test_case_op.number}:
Expected list: """, file=outfil, end='', )
                    print(f"""( {", ".join(map(str, test_case_op.expected_list))} )""", file=outfil)
                    print("""Actual list:  """,
                          file=outfil,
                          end=' ', )
                    self.print_list(num_list, outfil)
                    return False

                # Advance to the next node
                user_node = user_node.get_next()

                # Increment the index, which is used only for failure feedback
                index += 1

            # List += 1 operation succeeded
            print(f"""PASS: {'Inserting' if test_case_op.is_insertion else 'Removing'} {test_case_op.number} yields """,
                  file=outfil, end='', )
            if 0 == len(test_case_op.expected_list):
                print('an empty list.', file=outfil,)
            else:
                self.print_list(num_list, outfil,)
        print(f"""PASS: {len(self.operations)} list operations succeeded""",
              file=outfil,)

        return True

    # Prints a SortedNumberList's contents from head to tail. The
    # SortedNumberList's linked list must not have any circular references.
    def print_list(self,
                   num_list,
                   outfil,
                   separator = ",",
                   prefix = "( ",
                   suffix = " )",
                   ):
        # Print the prefix first
        print(prefix, file=outfil, end='', )

        # Get the list's head node
        node = num_list.head

        # If the head node is not null, prthe head node's data without any
        # separator and advance to next node.
        if node:
            print(node.get_data(), file=outfil, end='', )
            node = node.get_next()

        # Print each remaining node's data preceded by the separator
        while node:
            print(separator, node.get_data(), file=outfil, end='', )
            node = node.get_next()

        # Print the suffix last
        print(suffix, file=outfil)
