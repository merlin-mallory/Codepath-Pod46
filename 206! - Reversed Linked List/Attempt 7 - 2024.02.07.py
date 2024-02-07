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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/reverse-linked-list/

        Given the head of a singly linked list, reverse the list, and return the reversed list.

        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]

        Input: head = [1,2]
        Output: [2,1]

        Input: head = []
        Output: []

        Constraints:
        The number of nodes in the list is the range [0, 5000].
        -5000 <= Node.val <= 5000
        """
        prev = None
        cur = head
        while cur:
            prev = cur.next
            cur.next = prev
            prev = cur
            cur = prev

        return prev

solution = Solution()
list_head = create_list([1,2,3,4,5])
reversed_list_head = solution.reverseList(list_head)
print_list(reversed_list_head)  # Expected: [5,4,3,2,1]
