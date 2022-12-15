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

        Plan: explore_left and explore_right with DFS. At each step, verify that the explore.vals match,
        and that explore_left.left = explore_right.right, and that explore_left.right = explore_right.left. If
        there's a mismatch, then return False.
        '''
        # Failed attempt. Instead of explore_left and explore_right, I should be doing explore1 and explore2 inside
        # the mirror helper. explore1 is is_mirror_helper(root.left, root.right), while explore2 is is_mirror_helper(
        # root.right, root.left). Also, I don't need to verify the values of the children's nodes, it's enough to
        # simply check for existence of the correct numbers, the recursion will handle the value verfication.
        #
        # So base case 1: if left and right, then return True.
        # Base case 2: if not left or not right, then return False.
        # Base case 3: if left.val != right.val, then return False.
        # Recursion 1: Call is_mirror_helper(left.right, right.left)
        # Recursion 2: Call is_mirror_helper(left.left, right.right)
        # If recursion1 and recursion2 are True, then return True. Otherwise return false.

        if not root:
            return True

        def is_mirror_helper(left_node, right_node):
            if not left_node and not right_node:
                return True

            if not left_node or right_node:
                return False

            if left_node.val != right_node.val:
                return False

            if left_node.left != right_node.right:
                return False

            if left_node.right != right_node.left:
                return False

            return True

        result = is_mirror_helper(root.left, root.right)
        explore_left = self.isSymmetric(root.left)
        explore_right = self.isSymmetric(root.right)

        if result and explore_left and explore_right:
            return True
        else:
            return False
