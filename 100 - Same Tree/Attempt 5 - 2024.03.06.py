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

        Tree Traversal DFS
        Base Case 1: If not p and not q, return True.
        Base Case 2: If p and not q, return False.
        Base Case 3: If q and not p, return False
        Base Case 4: If p.val != q.val, return False
        return (self.isSameTree(p.left, q.left) and (self.isSameTree(p.right, q.right)
        '''
        if (not p) and (not q): return True
        if p and (not q): return False
        if q and (not p): return False
        if p.val != q.val: return False
        left_bool = self.isSameTree(p.left, q.left)
        right_bool = self.isSameTree(p.right, q.right)
        if left_bool and right_bool:
            return True
        else:
            return False
