from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(elements: List[int]) -> Optional[ListNode]:
    """
    Convert an array of elements into a linked list and return the head of the list.
    """
    head = None
    current = None
    for element in elements:
        if not head:
            head = ListNode(element)
            current = head
        else:
            current.next = ListNode(element)
            current = current.next
    return head

def print_list(head: Optional[ListNode]) -> None:
    """
    Print the elements of a linked list.
    """
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        You are given the head of a singly linked-list. The list can be represented as:

        L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form:

        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        You may not modify the values in the list's nodes. Only nodes themselves may be changed.

        Example 1:
        Input: head = [1,2,3,4]
        Output: [1,4,2,3]

        Example 2:
        Input: head = [1,2,3,4,5]
        Output: [1,5,2,4,3]

        Constraints:
        The number of nodes in the list is in the range [1, 5 * 104].
        1 <= Node.val <= 1000

        Do not return anything, modify head in-place instead.

        Plan:
        Linked List Traversal
        Find the midpoint with the slow/fast pointer method.
        Set right_seg to slow.next.
        Set slow.next to None.
        Set left_seg to head.
        Reverse right_seg
        Loop through left_seg and right seg.
            Set temp_left = left_seg.next
            Set temp_right = right_seg.next
            Set left_seg.next = right_seg
            Set right_seg.next = temp_left
            Set left_seg.next to temp_left.
            Set right_seg.next to temp_right.
        Return nothing
        Time: O(n)
        Space: O(1)
        Edge: Could only be 1 node in head.
        """
        # Locate the midpoint of the LL.
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Establish left and right segments
        right_seg = slow.next
        slow.next = None
        left_seg = head

        # Reverse right_seg
        prev = None
        cur = right_seg
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        right_seg = prev

        # Stitch left_seg and right_seg together
        while left_seg and right_seg:
            temp_left = left_seg.next
            temp_right = right_seg.next
            left_seg.next = right_seg
            right_seg.next = temp_left
            left_seg = temp_left
            right_seg = temp_right




solution = Solution()
list_head = create_list([1, 2, 3, 4])
solution.reorderList(list_head)
print_list(list_head)  # Expected: [1,4,2,3]

list_head = create_list([1, 2, 3, 4, 5])
solution.reorderList(list_head)
print_list(list_head)  # Expected: [1,5,2,4,3]
