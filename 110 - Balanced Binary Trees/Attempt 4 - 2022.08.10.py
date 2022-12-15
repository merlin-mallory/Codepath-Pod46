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
        '''
        # Failed attempt. I should make a find_height function that returns -1 if there isn't a root, and otherwise
        # returns 1+max(left_child_height, right_child_height). This will return the height of any given node. Then
        # we can use the function to explore_left and explore_right, and check for the differential. In addition we
        # need to check if every node is balanced, so we'll recursively call isBalanced on both the left child and
        # right child, and if either of those returns False, then our final result will be False. Otherwise
        # everything will be True.

        if not root:
            return True

        if root.left is None and root.right is None:
            return True

        explore_left = self.isBalanced(root.left)
        explore_right = self.isBalanced(root.right)

        if explore_left is True and explore_right is True:
            return True
        else:
            return False
