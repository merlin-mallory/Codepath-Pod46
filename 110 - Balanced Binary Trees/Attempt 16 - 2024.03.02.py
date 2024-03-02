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
        Tree Recursion DFS
        Create dfs(node) function.
            Base Case 1: If not node, return [True, -1]
            Recursive Case 1: left_bool, left_h = isBalanced(node.left)
            Recursive Case 2: right_bool, right_h = isBalanced(node.right)
            cur_height = 1 + max(left_h, right_h)
            if left_bool and right_bool and (abs(left_h - right_h) <= 1), return [True, cur_height]
            Else return [False, cur_height]
        Return dfs(root)[0]
        Time: O(n)
        Space: O(h)
        Edge: Could be zero nodes in root
        '''
        def dfs(node):
            if not node: return [True, -1]
            left_bool, left_h = dfs(node.left)
            right_bool, right_h = dfs(node.right)
            cur_h = 1 + max(left_h, right_h)
            if left_bool and right_bool and (abs(left_h - right_h) <= 1):
                return [True, cur_h]
            else:
                return [False, cur_h]
        return dfs(root)[0]
