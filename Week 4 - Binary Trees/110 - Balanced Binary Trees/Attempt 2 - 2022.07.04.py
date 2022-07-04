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
        -104 <= Node.val <= 104

        1. Explore the root.left and root.right with DFS recursion. We want to return up the height of each node.
        2. If we traverse the entire tree and root.left's height exceeds root.right's height by more than 1,
        then return False. Otherwise, return True.
        '''
        if not root:
            return True

        height_diff = abs(self.find_height(root.left) - self.find_height(root.right))
        if height_diff > 1:
            return False

        if self.isBalanced(root.left) is False:
            return False

        if self.isBalanced(root.right) is False:
            return False

        return True

    def find_height(self, root: TreeNode):
        if not root:
            return -1
        return 1 + max(self.find_height(root.left), self.find_height(root.right))


        # Failed attempt
        # if not root:
        #     return True
        # if root.left is None and root.right is None:
        #     return True
        #
        # def helper(root):
        #     if root is None:
        #         return 0, True
        #     if root.left is None and root.right is None:
        #         return 1, True
        #     if root.left is None and root.right is not None:
        #         return 0, False
        #     if root.left is not None and root.right is None:
        #         return 0, False
        #
        #     left_height, is_left_balanced = helper(root.left)
        #     right_height, is_right_balanced = helper(root.right)
        #
        #     height_diff = abs(left_height-right_height)
        #
        #     if height_diff <= 1 and is_left_balanced and is_right_balanced:
        #         return max(left_height, right_height)+1, True
        #     else:
        #         return max(left_height, right_height)+1, False
        #
        # left_height, is_left_balanced = helper(root.left)
        # right_height, is_right_balanced = helper(root.right)
        #
        # height_diff = abs(left_height-right_height)
        #
        # if height_diff <= 1 and is_left_balanced and is_right_balanced:
        #     return True
        # else:
        #     return False
        #
        #
