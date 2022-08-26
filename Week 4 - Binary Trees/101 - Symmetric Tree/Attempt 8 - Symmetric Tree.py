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
        1. We need to verify 3 things for every node: The location and number of children on both sides of the mirror
        needs to be the same, and also the values on both sides need to be the same. If any one of those things
        mismatches, then we can immediately return False. Otherwise, if we explore the entire tree without returning
        False, then we've verified that the tree is symmetric, so we will return True.
        '''
        return self.helper(root, root)

    def helper(self, left, right):
        if left and not right:
            return False
        if right and not left:
            return False
        if not left and not right:
            return True

        if left.val != right.val:
            return False

        explore_left = self.helper(left.left, right.right)

        if explore_left is False:
            return False

        explore_right = self.helper(left.right, right.left)

        if explore_right is False:
            return False

        return True
