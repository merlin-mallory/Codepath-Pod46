# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        110 - Balanced Binary Tree

        https://leetcode.com/problems/balanced-binary-tree/

        Given a binary tree, determine if it is height-balanced.

        For this problem, a height-balanced binary tree is defined as:
        a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

        Input: root = [3,9,20,null,null,15,7]
        Output: true

        Input: root = [1,2,2,3,3,null,null,4,4]
        Output: false

        Input: root = []
        Output: true

        Constraints:
        The number of nodes in the tree is in the range [0, 5000].
        -10^4 <= Node.val <= 10^4

        Plan:
        Tree Recursion
        Helper function
        Base Case: If there isn't a node, then return [True, 0].
        Recursive Case 1: bool_l, lh = isBalanced(lh.left)
        Recursive Case 2: bool_r, rh = isBalanced(lh.right)
        if bool_l and bool_r and (abs(lh - rh) <= 1:
            return [True, 1+max(lh, bh)]
        else:
            return [False, 1+max(lh, bh)]
        Call helper function, set equal to result, return result[0]
        Time: O(n)
        Space: O(n) worst case, O(log(n)) best case.
        Edge: Could be 0 nodes in root.
        '''
        def recurse_tree(node):
            if not node:
                return [True, 0]
            lh = recurse_tree(node.left)
            rh = recurse_tree(node.right)
            balanced =  lh[0] and rh[0] and (abs(lh[1] - rh[1]) <= 1)
            return [balanced, 1+max(lh[1], rh[1])]

        return recurse_tree(root)[0]
