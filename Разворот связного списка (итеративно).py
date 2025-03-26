from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a linked list iteratively.

    Args:
        head: The head node of the linked list to reverse.

    Returns:
        The head node of the reversed linked list.
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

def list_to_linked_list(lst: list) -> Optional[ListNode]:
    """Helper function to convert a list to a linked list."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Helper function to convert a linked list to a list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
        # Test case 1: Normal case
        input_list = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        head = list_to_linked_list(input_list)
        reversed_head = reverse_linked_list(head)
        self.assertEqual(linked_list_to_list(reversed_head), expected)
        
        # Test case 2: Empty list
        self.assertIsNone(reverse_linked_list(None))
        
        # Test case 3: Single element
        input_list = [1]
        expected = [1]
        head = list_to_linked_list(input_list)
        reversed_head = reverse_linked_list(head)
        self.assertEqual(linked_list_to_list(reversed_head), expected)
        
        # Test case 4: Two elements
        input_list = [1, 2]
        expected = [2, 1]
        head = list_to_linked_list(input_list)
        reversed_head = reverse_linked_list(head)
        self.assertEqual(linked_list_to_list(reversed_head), expected)

if __name__ == "__main__":
    unittest.main()
