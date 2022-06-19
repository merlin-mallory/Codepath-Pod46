# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Input: head = [1,2,3,4,5], k = 2
        Output: [4,5,1,2,3]

        Input: head = [0,1,2], k = 4
        Output: [2,0,1]

        Constraints:

        The number of nodes in the list is in the range [0, 500].
        -100 <= Node.val <= 100
        0 <= k <= 2 * 109

        Plan 1:
        1. Calculate length of LL.
        2. Calculate necessary_rotations. k % len(head)
        3. Perform the swap necessary_rotations times.
        4. Time Complexity: O(n * necessary_rotations)
        5. Space Complexity: O(1)

        Plan 2:
        1. Calculate length of LL.
        2. Calculate necessary_rotations. k % len(head)
        3. Create a new LL right.
        4. Iterate through the head necessary_rotations times, collecting nodes in new LL right.
        5. Create a new LL left.
        6. Iterate through the remaining nodes in the head, collecting nodes in new LL left.
        7. Merge new LL left with new LL right, and return LL left head.
        8. Time complexity: O(n)
        9. Space complexity: O(n)

        Plan 3:
        1. Handle base cases. If no head, return None. If no head.next, return head.
        2. Iterate through head, grabbing the front node, back node, and calculate the length of the list.
        3. Set back.next = head (creates a cycle)
        4. Calculate the new head (n - k % n), and new tail (n - k % n - 1)
        5. Find the new_tail (iterate (n - k % n - 1)).
        6. Set the new_head to new_tail.next
        7. Set the new_tail.next to None
        8. Return the new_head.
        9. Time complexity: O(n)
        10.Space complexity: O(1)
        '''

        if not head:
            return

        if not head.next:
            return head

        old_head = head
        old_tail = head
        n = 1

        while old_tail.next:
            n += 1
            old_tail = old_tail.next

        old_tail.next = old_head

        new_tail_pos = n - (k % n) - 1

        new_tail = old_head
        for i in range(new_tail_pos):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head