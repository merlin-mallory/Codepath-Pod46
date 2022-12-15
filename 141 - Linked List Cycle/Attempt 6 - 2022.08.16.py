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
        1. Slow/fast pointers. Slow = head, fast = head.next.
        2. Until fast or fast.next or fast.next.next equals none or slow=fast, iterate slow once, and fast twice.
        3. If slow = fast, return True. Otherwise, return false.
        '''
        if not head:
            return False

        slow, fast = head, head.next
        while fast and fast.next and fast.next.next and slow != fast:
            slow = slow.next

            if fast.next is None:
                fast = fast.next
            elif fast.next.next:
                fast = fast.next.next

        return slow == fast
