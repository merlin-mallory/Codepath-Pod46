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
        1. Create two objects, one exploring the left side of the tree, and the other exploring the right side of the
        tree. Swap left_side.left with right_side.right, and swap left_side.right with right_side.right. We keep
        swapping until we reach leaf nodes.
        2. Time: O(n), Space: O(1)
        '''
        if not root:
            return None

        if root.left and root.right:
            temp = root.left
            root.left = root.right
            root.right = temp

        elif root.left:
            root.right = root.left
            root.left = None

        elif root.right:
            root.left = root.right
            root.right = None

        if root.left:
            root.left = self.invertTree(root.left)

        if root.right:
            root.right = self.invertTree(root.right)

        return root
