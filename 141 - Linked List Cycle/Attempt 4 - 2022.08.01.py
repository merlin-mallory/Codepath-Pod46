# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        https://leetcode.com/problems/linked-list-cycle/

        Given head, the head of a linked list, determine if the linked list has a cycle in it.

        There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
        following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
        is connected to. Note that pos is not passed as a parameter.

        Return true if there is a cycle in the linked list. Otherwise, return false.

        Input: head = [3,2,0,-4], pos = 1
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

        Input: head = [1,2], pos = 0
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

        Input: head = [1], pos = -1
        Output: false
        Explanation: There is no cycle in the linked list.

        The number of the nodes in the list is in the range [0, 10^4].
        -10^5 <= Node.val <= 10^5
        pos is -1 or a valid index in the linked-list.

        Plan:
        1. Slow/fast pointers
        2. slow_pointer = head, fast_pointer = head.next.
        3. If slow_pointer == fast_pointer, then there is a cycle, so return True.
        4. If the fast_pointer, fast_pointer.next, or fast_pointer.next.next is None, then we've reached the end of LL
        and verified there is not a cycle, so return False.
        5. slow_pointer+1, fast_pointer+2
        '''
        if not head or head.next is None:
            return False

        slow_pointer = head
        fast_pointer = head.next

        while fast_pointer is not None:
            if slow_pointer == fast_pointer:
                return True

            slow_pointer = slow_pointer.next
            if fast_pointer.next is None:
                fast_pointer = None
            else:
                fast_pointer = fast_pointer.next.next

        return False
