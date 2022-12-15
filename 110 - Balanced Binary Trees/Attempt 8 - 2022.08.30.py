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
        1. Make a calculate_height function. This will take a node, and return the maximum height of its left and
        right children. Probably use tail recursion, returning -1 if the current node is node.
        2. Traverse the tree with in-order DFS. At each node, calculate the height of the left child and the height
        of the right child. If the absolute difference of the two is >1, then immediately return false.
        3. If we finish the tree traversal without returning false, then we've confirmed that the tree is balanced,
        so return True.
        '''
        if not root:
            return True

        explore_left = self.isBalanced(root.left)
        if explore_left is False:
            return False

        explore_right = self.isBalanced(root.right)
        if explore_right is False:
            return False

        left_height = self.calculate_height(root.left)
        right_height = self.calculate_height(root.right)
        abs_diff = abs(left_height - right_height)

        if abs_diff > 1:
            return False
        else:
            return True

    def calculate_height(self, node):
        if not node:
            return -1
        return 1 + max(self.calculate_height(node.left), self.calculate_height(node.right))
