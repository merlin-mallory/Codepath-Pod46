# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        https://leetcode.com/problems/symmetric-tree/description/
        Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

        Input: root = [1,2,2,3,4,4,3]
        Output: true

        Input: root = [1,2,2,null,3,null,3]
        Output: false

        Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        -100 <= Node.val <= 100

        Plan:
        1. There are three conditions that must be met. First, the left child and right child must have the same
        number of nodes. Second, the left child and right child must have the same values. If there's a mismatch,
        return False, Otherwise, return True.
        '''
        return self.helper(root, root)

    def helper(self, left_node, right_node):
        if not left_node and not right_node:
            return True
        if left_node and not right_node:
            return False
        if right_node and not left_node:
            return False
        if left_node.val != right_node.val:
            return False

        explore_left = self.helper(left_node.left, right_node.right)
        explore_right = self.helper(left_node.right, right_node.left)

        if explore_left and explore_right:
            return True
        else:
            return False



