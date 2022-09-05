# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
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
        1. Make a calculate_height function. It will take a node, and return the max height of either the left or
        right child.
        2. Post-order DFS the tree, and confirm that abs(left_height - right_height) is never greater than 1
        '''
        if not root:
            return True

        explore1 = self.isBalanced(root.left)
        if not explore1:
            return False
        explore2 = self.isBalanced(root.right)
        if not explore2:
            return False

        height_diff = abs(self.calculate_height(root.left) - self.calculate_height(root.right))
        if height_diff > 1:
            return False
        else:
            return True

    def calculate_height(self, node):
        if not node:
            return -1
        return 1 + max(self.calculate_height(node.left), self.calculate_height(node.right))