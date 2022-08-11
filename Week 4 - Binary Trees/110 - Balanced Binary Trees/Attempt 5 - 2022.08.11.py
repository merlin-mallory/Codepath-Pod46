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

        1. Make a calculate_height function. It will return 1 + max height of both the left child and right child.
        When we reach a leaf node, return -1. to balance out the height.
        2. Traverse the tree with DFS. Calcluate the left_child_height and right_child_height. If the absolute
        difference is >= 1, then return False. Otherwise, if we traverse the entire tree and the differential never
        exceeds 1, then return true.
        '''
        # Partial success. I had to adjust the base cases in both calculate height (from not node.left and not
        # node.right to not nod) and also isBalanced (from if height_difference >= 1 to height_difference > 1).
        if not root:
            return True

        explore_left = self.isBalanced(root.left)
        explore_right = self.isBalanced(root.right)
        height_difference = abs(self.calculate_height(root.left) - self.calculate_height(root.right))
        if height_difference > 1:
            return False

        if explore_left and explore_right:
            return True
        else:
            return False

    def calculate_height(self, node):
        if not node:
            return -1
        return 1 + max(self.calculate_height(node.left), self.calculate_height(node.right))
