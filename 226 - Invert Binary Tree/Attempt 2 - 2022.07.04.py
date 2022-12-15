# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        https://leetcode.com/problems/invert-binary-tree/

        Given the root of a binary tree, invert the tree, and return its root.

        Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]

        Input: root = [2,1,3]
        Output: [2,3,1]

        Input: root = []
        Output: []

        Constraints:

        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100

        Plan:
        1. Create a new tree set to root, and then set the original.left to new.right, and the original.right to
        the new.left.
        2. Loop down the entire tree until we hit leaf nodes.
        3. Return the final tree
        '''
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root


        # Failed attempt
        # def helper(root):
        #     if root.left is None and root.right is None:
        #         return root
        #
        #     root.left = helper(root.right)
        #
        #     temp = root.left
        #     root.left = root.right
        #     root.right = temp
        #
        #     root.left = helper(root.right)
        #
        #     return root
        #
        # if root is None:
        #     return None
        #
        # return helper(root)