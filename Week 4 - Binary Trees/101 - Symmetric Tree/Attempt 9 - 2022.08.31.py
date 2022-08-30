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
        1. In order for a node to be symmetric, the left side node value must be the same as the right node value.
        And also, the left node's children must mirror the right node's children. If any one of those conditions
        breaks, then return false. Otherwise, return true.
        '''
        return self.helper(root, root)

    def helper(self, left, right):
        if not left and not right:
            return True
        if left and not right:
            return False
        if right and not left:
            return False
        if left.val != right.val:
            return False

        explore_left = self.helper(left.left, right.right)
        explore_right = self.helper(left.right, right.left)

        if explore_left and explore_right:
            return True
        else:
            return False
