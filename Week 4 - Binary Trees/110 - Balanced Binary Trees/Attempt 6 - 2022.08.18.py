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
        1. Make a calculate_height function. This will take a node, and return the height of the node's largest child.
        2. Traverse the entire tree with DFS and verify that every node is height balanced.
        '''
        if not root:
            return True

        explore_left = self.isBalanced(root.left)
        explore_right = self.isBalanced(root.right)

        height_of_left_child = self.calculate_height(root.left)
        height_of_right_child = self.calculate_height(root.right)

        if abs(height_of_left_child - height_of_right_child) <= 1 and explore_left and explore_right:
            return True
        else:
            return False

    def calculate_height(self, node):
        if not node:
            return -1

        height_of_left_child = 1 + self.calculate_height(node.left)
        height_of_right_child = 1 + self.calculate_height(node.right)
        return max(height_of_left_child, height_of_right_child)
