from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        100 - Same Tree

        https://leetcode.com/problems/same-tree/

        Given the roots of two binary trees p and q, write a function to check if they are the same or not.

        Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

        Example 1:
        Input: p = [1,2,3], q = [1,2,3]
        Output: true

        Example 2:
        Input: p = [1,2], q = [1,null,2]
        Output: false

        Example 3:
        Input: p = [1,2,1], q = [1,1,2]
        Output: false

        Constraints:
        The number of nodes in both trees is in the range [0, 100].
        -10^4 <= Node.val <= 10^4

        Plan:
        We need to verify that the height of each node is identical, and also that the values at each node are
        identical.
        '''
        if (not p) and (not q):
            return True

        if ((not p) and q) or (p and(not q)):
            return False

        if p.val != q.val:
            return False

        left_result = self.isSameTree(p.left, q.left)
        right_result = self.isSameTree(p.right, q.right)

        return left_result and right_result
