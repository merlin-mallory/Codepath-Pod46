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
        """
        # Locate midpoint with fast/slow pointers
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None
        l1 = head

        # Reverse L2
        prev = None
        cur = l2
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        l2 = prev

        # Weave l1 and l2 together
        while l1 and l2:
            temp_l1 = l1.next
            temp_l2 = l2.next

            l1.next = l2
            l2.next = temp_l1

            l1 = temp_l1
            l2 = temp_l2


solution = Solution()
list_head = create_list([1, 2, 3, 4])
solution.reorderList(list_head)
print_list(list_head)  # Expected: [1,4,2,3]

list_head = create_list([1, 2, 3, 4, 5])
solution.reorderList(list_head)
print_list(list_head)  # Expected: [1,5,2,4,3]
