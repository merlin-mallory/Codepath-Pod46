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
        We need to travel through the entire tree and confirm that each node is height-balanced. If at any point an
        imbalance is detected, we should return False up the tree. Otherwise, we should return True.
        cur_bool = [True]
        Create recurseTree(node)
            If there's not a node, then return 0.
            left_bool, left_height = recurseTree(node.left)
            right_bool, right_height = recurseTree(node.right)
            cur_height = 1 + max(left_height, right_height)
            if left_bool and right_bool and (abs(left_height - right_height) <= 1):
                return [True, cur_height]
            else
                return [False, cur_height]
        Call recurseTree(root), set equal to result
        Return result[0]
        '''
        def recurseTree(node):
            if not node:
                return [True, 0]
            left_bool, left_height = recurseTree(node.left)
            right_bool, right_height = recurseTree(node.right)
            cur_height = 1 + max(left_height, right_height)
            if left_bool and right_bool and (abs(left_height - right_height) <= 1):
                return [True, cur_height]
            else:
                return [False, cur_height]

        result = recurseTree(root)
        return result[0]