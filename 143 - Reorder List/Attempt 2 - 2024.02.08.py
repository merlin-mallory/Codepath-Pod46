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
        Linked List
        1. Locate the halfway point with slow/fast pointer method.
        2. Set right_half to slow.next. Set slow.next to none.
        3. Reverse right_half.
        4. Loop through left_half and right_half, rewiring pointers as we go
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right_half = slow.next
        slow.next = None

        # Reverse the right half
        prev = None
        cur = right_half
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        right_half = prev

        left_half = head
        # Loop through head and right_half
        while left_half and right_half:
            # Grab the next values of both left and right before we rewire them.
            left_half_temp = left_half.next
            right_half_temp = right_half.next

            # Append the right_half to the left_half, and the left_half_temp to the right_half.
            left_half.next = right_half
            right_half.next = left_half_temp

            # Advance the pointers forward. So now the left_half has all of its unprocessed nodes back, and so does
            # right_half.
            left_half = left_half_temp
            right_half = right_half_temp


solution = Solution()
list_head = create_list([1, 2, 3, 4])
solution.reorderList(list_head)
print_list(list_head)  # Expected: [1,4,2,3]

list_head = create_list([1, 2, 3, 4, 5])
solution.reorderList(list_head)
print_list(list_head)  # Expected: [1,5,2,4,3]
