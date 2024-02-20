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
        Recursive Tree
        In order to check of the tree is balanced, we need to check that the height of the left node and the height
        of the right node differ by no more than 1.
        So we can recurse down to the left and right, and calculate heights going from the root nodes upwards.
        So we need to return up a boolean as well as the current height, so we'll need a helper function
        '''
        def helper(node):
            if not node:
                return [True, 0]
            l_bool, l_height = helper(node.left)
            r_bool, r_height = helper(node.right)
            if l_bool and r_bool and (abs(l_height - r_height) <= 1):
                return [True, 1 + max(l_height, r_height)]
            else:
                return [False, 1 + max(l_height, r_height)]

        result = helper(root)
        return result[0]