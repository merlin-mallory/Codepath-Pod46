# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        543 - Diameter of Binary Tree

        https://leetcode.com/problems/diameter-of-binary-tree/

        Given the root of a binary tree, return the length of the diameter of the tree.

        The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path
        may or may not pass through the root.

        The length of a path between two nodes is represented by the number of edges between them.

        Example 1:
        Input: root = [1,2,3,4,5]
        Output: 3
        Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

        Example 2:
        Input: root = [1,2]
        Output: 1

        Constraints:
        The number of nodes in the tree is in the range [1, 10^4].
        -100 <= Node.val <= 100

        Plan:
        Tree Recursion
        max_dia = [0]
            Base Case: If not root, return 0
            Recurse 1: left_height = recurse(root.left)
            Recurse 2: right_height = recurse(root.right)
            Work1: cur_height = 1 + max(left_height, right_height)
            Work2: cur_dia = 2 + left_height + right_height
            Work3: Update max_dia
            Return cur_height
        Call recurse(root)
        return max_dia[0]
        '''
        max_dia = [0]
        def recurseTree(node):
            if not node:
                return -1
            left_height = recurseTree(node.left)
            right_height = recurseTree(node.right)
            cur_height = 1 + max(left_height, right_height)
            cur_dia = 2 + left_height + right_height
            max_dia[0] = max(max_dia[0], cur_dia)
            return cur_height
        recurseTree(root)
        return max_dia[0]

