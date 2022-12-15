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
        1. Two recursive calls, explore_left and explore_right.
        2. Swap explore_left with explore_right. Then swap each explore's children
        '''
        def helper(current):
            if not current:
                return None
            new_left = helper(current.right)
            new_right = helper(current.left)
            current.left = new_left
            current.right = new_right
            return current

        return helper(root)
