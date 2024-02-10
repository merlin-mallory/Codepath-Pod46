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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Given the head of a linked list, remove the nth node from the end of the list and return its head.

        Example 1:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]

        Example 2:
        Input: head = [1], n = 1
        Output: []

        Example 3:
        Input: head = [1,2], n = 1
        Output: [1]

        Constraints:
        The number of nodes in the list is sz.
        1 <= sz <= 30
        0 <= Node.val <= 100
        1 <= n <= sz

        Follow up: Could you do this in one pass?

        Plan:
        Set dummy = head
        Do slow and fast pointers to locate the nth spot of the head.
        Keep track of the slow's previous, and set slow.prev to slow.next to essential delete the desired node
        Return the dummy.
        '''
        # if head.next is None:
        #     return None

        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while fast and n > 0:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next


solution = Solution()
list_head = create_list([1,2,3,4,5])
new_list_head = solution.removeNthFromEnd(list_head, 2)
print_list(new_list_head)  # Expected: [1,2,3,5]

list_head = create_list([1])
new_list_head = solution.removeNthFromEnd(list_head, 1)
print_list(new_list_head)  # Expected: []

list_head = create_list([1,2])
new_list_head = solution.removeNthFromEnd(list_head, 1)
print_list(new_list_head)  # Expected: [1]

list_head = create_list([1,2])
new_list_head = solution.removeNthFromEnd(list_head, 2)
print_list(new_list_head)  # Expected: [2]
