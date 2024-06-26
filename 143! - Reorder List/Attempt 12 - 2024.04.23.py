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
        Time: O(n)
        Space: O(1)
        Edge: None
        """
        # Locate the midpoint, separate left_seg and right_seg
        dummy = ListNode(-1, head)
        slow = dummy.next
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right_seg = slow.next
        slow.next = None
        left_seg = dummy.next


        # Reverse the right_seg
        prev = None
        cur = right_seg
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        right_seg = prev

        # Merge the left_seg and right_seg
        while left_seg and right_seg:
            left_seg_temp = left_seg.next
            right_seg_temp = right_seg.next
            left_seg.next = right_seg
            right_seg.next = left_seg_temp
            left_seg = left_seg_temp
            right_seg = right_seg_temp


solution = Solution()
list_head = create_list([1, 2, 3, 4])
solution.reorderList(list_head)
print_list(list_head)  # Expected: [1,4,2,3]

list_head = create_list([1, 2, 3, 4, 5])
solution.reorderList(list_head)
print_list(list_head)  # Expected: [1,5,2,4,3]
