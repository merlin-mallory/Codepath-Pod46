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

        Tree Recursion with DFS
        Create dfs(node)
            Base Case 1: If not node, return True.
            left_bool, left_height = isBalanced(root.left)
            right_bool, right_height = isBalanced(root.right)
            cur_height = 1 + max(left_height, right_height)
            if left_bool and right_bool and (abs(left_height - right_height) <= 1):
                return [True, cur_height]
            else:
                return [False, 0]
        Return dfs(root)[0]
        '''
        def dfs(node):
            if not node: return [True, 0]
            left_bool, left_height = dfs(node.left)
            right_bool, right_height = dfs(node.right)
            cur_height = 1 + max(left_height, right_height)
            if left_bool and right_bool and (abs(left_height - right_height) <= 1):
                return [True, cur_height]
            else:
                return [False, cur_height]
        return dfs(root)[0]