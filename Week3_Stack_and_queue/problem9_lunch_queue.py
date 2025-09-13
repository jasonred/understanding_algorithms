def countStudents(students: list[int], sandwiches: list[int]) -> int:
    """
    Count the number of students who cannot eat lunch.
    
    Students queue up for lunch. Each student prefers a sandwich type (0 or 1).
    Sandwiches are stacked; the top is served first. If the front student doesn't want
    the top sandwich, they go to the end of the queue. This continues until no student
    at the front wants the top sandwich. Return the number of students who cannot eat.
    
    Time Complexity: O(n) where n is the number of students
    Space Complexity: O(n) for the queue
    
    Args:
        students: List of student preferences (0 or 1)
        sandwiches: List of sandwich types (0 or 1), top sandwich is first
        
    Returns:
        int: Number of students who cannot eat
    """
    if not students or not sandwiches:
        return len(students)
    
    # Use deque for efficient queue operations
    from collections import deque
    
    # Create queue from students list
    student_queue = deque(students)
    sandwich_stack = sandwiches.copy()
    
    # Track consecutive rotations without serving
    consecutive_rotations = 0
    
    while student_queue and sandwich_stack:
        # Get front student and top sandwich
        front_student = student_queue[0]
        top_sandwich = sandwich_stack[0]
        
        if front_student == top_sandwich:
            # Student gets their preferred sandwich
            student_queue.popleft()  # Remove student from queue
            sandwich_stack.pop(0)    # Remove sandwich from stack
            consecutive_rotations = 0  # Reset rotation counter
        else:
            # Student doesn't want this sandwich, move to back of queue
            student_queue.rotate(-1)  # Move front to back
            consecutive_rotations += 1
            
            # If we've rotated through the entire queue without serving anyone,
            # no one can eat the remaining sandwiches
            if consecutive_rotations == len(student_queue):
                break
    
    # Return number of students still in queue (cannot eat)
    return len(student_queue)


def countStudents_optimized(students: list[int], sandwiches: list[int]) -> int:
    """
    Optimized version using counting instead of simulation.
    
    Instead of simulating the queue, we can count the preferences and
    determine how many students cannot be served based on sandwich availability.
    
    Time Complexity: O(n) where n is the number of students
    Space Complexity: O(1) - only using a few variables
    """
    if not students or not sandwiches:
        return len(students)
    
    # Count student preferences
    student_count = [0, 0]  # [count_of_0_preferences, count_of_1_preferences]
    for student in students:
        student_count[student] += 1
    
    # Process sandwiches in order
    for sandwich in sandwiches:
        if student_count[sandwich] > 0:
            # Serve this sandwich to a student who wants it
            student_count[sandwich] -= 1
        else:
            # No student wants this sandwich type, stop processing
            break
    
    # Return remaining students who cannot eat
    return student_count[0] + student_count[1]


def countStudents_with_queue_simulation(students: list[int], sandwiches: list[int]) -> int:
    """
    Alternative implementation using manual queue simulation with list.
    This version doesn't use deque for educational purposes.
    
    Time Complexity: O(n) where n is the number of students
    Space Complexity: O(n) for the queue
    """
    if not students or not sandwiches:
        return len(students)
    
    # Create copies to avoid modifying input
    student_queue = students.copy()
    sandwich_stack = sandwiches.copy()
    
    consecutive_rotations = 0
    
    while student_queue and sandwich_stack:
        front_student = student_queue[0]
        top_sandwich = sandwich_stack[0]
        
        if front_student == top_sandwich:
            # Serve the student
            student_queue.pop(0)
            sandwich_stack.pop(0)
            consecutive_rotations = 0
        else:
            # Move student to back of queue
            student_queue.append(student_queue.pop(0))
            consecutive_rotations += 1
            
            # Check if we've gone through entire queue without serving
            if consecutive_rotations == len(student_queue):
                break
    
    return len(student_queue)


# Test cases
def test_count_students():
    """Test the implementation with various cases."""
    
    # Test case 1: Example from problem
    students1 = [1, 1, 0, 0]
    sandwiches1 = [0, 1, 0, 1]
    result1 = countStudents(students1, sandwiches1)
    print(f"Test 1: students={students1}, sandwiches={sandwiches1} -> {result1} (expected: 0)")
    
    # Test case 2: More students than available sandwiches of their preferred type
    students2 = [1, 1, 1, 0, 0, 1]
    sandwiches2 = [1, 0, 0, 0, 0, 0, 1, 1]
    result2 = countStudents(students2, sandwiches2)
    print(f"Test 2: students={students2}, sandwiches={sandwiches2} -> {result2} (expected: 3)")
    
    # Test case 3: No students can eat
    students3 = [1, 1, 1, 1]
    sandwiches3 = [0, 0, 0, 0]
    result3 = countStudents(students3, sandwiches3)
    print(f"Test 3: students={students3}, sandwiches={sandwiches3} -> {result3} (expected: 4)")
    
    # Test case 4: All students can eat
    students4 = [0, 1, 0, 1]
    sandwiches4 = [0, 1, 0, 1]
    result4 = countStudents(students4, sandwiches4)
    print(f"Test 4: students={students4}, sandwiches={sandwiches4} -> {result4} (expected: 0)")
    
    # Test case 5: Mixed case
    students5 = [1, 0, 1, 0]
    sandwiches5 = [0, 1, 1, 0]
    result5 = countStudents(students5, sandwiches5)
    print(f"Test 5: students={students5}, sandwiches={sandwiches5} -> {result5} (expected: 0)")
    
    # Test case 6: Empty inputs
    students6 = []
    sandwiches6 = []
    result6 = countStudents(students6, sandwiches6)
    print(f"Test 6: students={students6}, sandwiches={sandwiches6} -> {result6} (expected: 0)")
    
    # Test case 7: Single student and sandwich
    students7 = [1]
    sandwiches7 = [0]
    result7 = countStudents(students7, sandwiches7)
    print(f"Test 7: students={students7}, sandwiches={sandwiches7} -> {result7} (expected: 1)")


def test_all_implementations():
    """Test all three implementations to ensure they produce the same results."""
    test_cases = [
        ([1, 1, 0, 0], [0, 1, 0, 1]),
        ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1]),
        ([1, 1, 1, 1], [0, 0, 0, 0]),
        ([0, 1, 0, 1], [0, 1, 0, 1]),
        ([1, 0, 1, 0], [0, 1, 1, 0]),
        ([], []),
        ([1], [0]),
        ([0, 0, 1, 1], [1, 1, 0, 0])
    ]
    
    print("Testing all implementations:")
    print("=" * 50)
    
    for i, (students, sandwiches) in enumerate(test_cases, 1):
        result1 = countStudents(students, sandwiches)
        result2 = countStudents_optimized(students, sandwiches)
        result3 = countStudents_with_queue_simulation(students, sandwiches)
        
        print(f"Test {i}: {result1}, {result2}, {result3} - {'✓' if result1 == result2 == result3 else '✗'}")


if __name__ == "__main__":
    print("Lunch Queue Problem Tests")
    print("=" * 40)
    test_count_students()
    print("\n")
    test_all_implementations()
