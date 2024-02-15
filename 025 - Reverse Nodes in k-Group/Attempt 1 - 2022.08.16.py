# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/reverse-nodes-in-k-group/

        Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

        k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is
        not a multiple of k then left-out nodes, in the end, should remain as it is.

        You may not alter the values in the list's nodes, only nodes themselves may be changed.

        Input: head = [1,2,3,4,5], k = 2
        Output: [2,1,4,3,5]

        Input: head = [1,2,3,4,5], k = 3
        Output: [3,2,1,4,5]

        Constraints:
        The number of nodes in the list is n.
        1 <= k <= n <= 5000
        0 <= Node.val <= 1000

        Plan:
        1. Make an is_reversible function. Takes a node, iterates k, records the next node (if any). If the final
        node is not None, then return the .next node as the tail_after_reverse.
        2. Make a reverse_LL_by_k function. Takes a node, and reverses that part of the LL, and returns the head of
        the newly reversed LL.
        3. In the core function, set previous = None, dummy = ListNode(-1), dummy.next = previous. call is_reversible
        on the current node. If it's true, then call reverse_LL_by_k. Set previous.next to the head of the reversed
        list. Then iterate k, and then set current.next = tail_after_reverse. Keep looping until tail_after_reverse
        is None.
        4. Return dummy.next
        """
        dummy = ListNode(0, head)
        left_seg = dummy

        def getKth(cur, k):
            while cur and k > 0:
                cur = cur.next
                k -= 1
            return cur

        while True:
            mid_seg = getKth(left_seg, k)
            if not mid_seg:
                break
            right_seg = mid_seg.next

            # reverse group
            prev, cur = mid_seg.next, left_seg.next
            while cur != right_seg:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            temp = left_seg.next
            left_seg.next = mid_seg
            left_seg = temp
        return dummy.next

    #     # Below is a O(n) time O(n/k) space solution.
    #     count = 0
    #     current = head
    #
    #     # First, see if there are atleast k nodes
    #     # left in the linked list.
    #     while count < k and current:
    #         current = current.next
    #         count += 1
    #
    #     # If we have k nodes, then we reverse them
    #     if count == k:
    #         # Reverse the first k nodes of the list and
    #         # get the reversed list's head.
    #         reversedHead = self.reverseLinkedList(head, k)
    #
    #         # Now recurse on the remaining linked list. Since
    #         # our recursion returns the head of the overall processed
    #         # list, we use that and the "original" head of the "k" nodes
    #         # to re-wire the connections.
    #         head.next = self.reverseKGroup(current, k)
    #         return reversedHead
    #     return head
    #
    # def reverseLinkedList(self, head, k):
    #     # Reverse k nodes of the given linked list.
    #     # This function assumes that the list contains
    #     # atleast k nodes.
    #     previous, current = None, head
    #     while k:
    #         # Keep track of the next node to process in the
    #         # original list
    #         temp = current.next
    #
    #         # Insert the node pointed to by "ptr"
    #         # at the beginning of the reversed list
    #         current.next = previous
    #         previous = current
    #
    #         # Move on to the next node
    #         current = temp
    #
    #         # Decrement the count of nodes to be reversed by 1
    #         k -= 1
    #
    #     # Return the head of the reversed list
    #     return previous

        # def is_reversible(current, k):
        #     for i in range(k-1):
        #         current = current.next
        #
        #     if current != None:
        #         can_reverse = True
        #         tail_after_reverse = current.next
        #     else:
        #         can_reverse = False
        #         tail_after_reverse = None
        #
        #     return (can_reverse, tail_after_reverse)
        #
        # def reverse_LL_by_k(current, k):
        #     previous = None
        #     for i in range(k):
        #         temp = current.next
        #         current.next = previous
        #         previous = current
        #         current = temp
        #     return previous
        #
        # previous = ListNode(-1)
        # current = head
        # dummy = previous
        #
        # while current:
        #     can_reverse, tail_after_reverse = is_reversible(current, k)
        #     if can_reverse:
        #         previous.next = reverse_LL_by_k(current, k)
        #         current = previous.next
        #         for i in range(k-1):
        #             current = current.next
        #         current.next = tail_after_reverse
        #
        #         previous = current
        #         current = current.next
        #
        # return dummy.next
