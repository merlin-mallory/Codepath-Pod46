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
        1. Create two objects, one for the left branch, and one for the right branch. Iterate down both objects
        simultanouesly, and if a mismatch is found, then return False. Otherwise, return true.
        '''

        def helper(left, right):
            if left is None and right is None:
                return True
            if left is None and right is not None:
                return False
            if left is not None and right is None:
                return False

            if left.val != right.val:
                return False

            left_result1 = helper(left.left, right.right)
            left_result2 = helper(left.right, right.left)

            if left_result1 and left_result2:
                return True
            else:
                return False


        left = root.left
        right = root.right

        return helper(left, right)
