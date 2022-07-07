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
        1. We will use the fast/slow pointer strategy. If the slow pointer reaches the end of the LL without matching
        the fast pointer, then we will know that we have a cycle in the LL.
        2. Set slow_pointer = head
        3. Set fast_pointer = head.next
        4. Loop through both pointers, iterating slow_pointer by 1, and fast_pointer by 2. If at any point they point
        to the same node, then return false. Otherwise, after the slow pointer reaches the tail, return True.
        5. Time: O(n), Space: O(1)
        '''

        if not head:
            return False

        if head.next is None:
            return False

        slow_pointer = head
        fast_pointer = head.next

        while slow_pointer.next is not None and fast_pointer.next is not None:
            if slow_pointer == fast_pointer:
                return True

            slow_pointer = slow_pointer.next
            if fast_pointer.next.next is not None:
                fast_pointer = fast_pointer.next.next
            elif fast_pointer.next is not None:
                fast_pointer = fast_pointer.next

        return False