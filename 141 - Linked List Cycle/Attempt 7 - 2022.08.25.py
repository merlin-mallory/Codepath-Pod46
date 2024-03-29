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
        1. Looks like fast/slow pointers.
        2. slow = head, fast = head.next
        3. while fast.next and fast.next.next are not None, move the slow pointer 1 node, and the fast pointer 2 nodes.
        4. If the loop breaks before slow == None, then we know there's not a cycle. Otherwise, at some point slow
        will equal fast.
        '''
        if not head:
            return False

        if head.next is None:
            return False

        slow, fast = head, head.next

        while fast.next is not None and fast.next.next is not None and slow != fast:
            slow = slow.next
            fast = fast.next.next

        return fast == slow
