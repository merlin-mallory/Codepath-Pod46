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
        1. There are 3 conditions for symmetry. The first is left.val == right.val. The second is left.left_child =
        right.right_child. The third is left.right_child = right.left_child. If all three conditions are met,
        then we can return True.
        2. Make a helper function which will take a node.left and node.right, and return True if all 3 conditions are
        met. Otherwise return False.
        3. Main function base case: If there's not a node, then return True. Return isSymmetric(root, root)
        '''
        # Failed attempt.

        if not root:
            return True

        if root.left:
            explore_left = self.isSymmetric(root.left)
        else:
            explore_left = None

        if root.right:
            explore_right = self.isSymmetric(root.left)
        else:
            explore_right = None

        result = self.calc_symmetry(root)

        if explore_left is False or explore_right is False or result is False:
            return False
        else:
            return True


    def calc_symmetry(self, node):
        if not node:
            return True
        if node.left is None and node.right is None:
            return True

        if node.left.val != node.right.val:
            return False
        if node.left.left != node.right.right:
            return False
        if node.left.right != node.right.left:
            return False
        return True
