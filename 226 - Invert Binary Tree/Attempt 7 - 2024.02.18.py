# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        226 - Invert Binary Tree

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
        Tree
        Recursively flip left and right. Return when we reach Null. Recursively call on both left and right.
        Time: O(n)
        Space: O(log(n)) best case, O(n) worst case.
        Edge: Could be 0 nodes in root.
        '''
        if not root:
            return None
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root

