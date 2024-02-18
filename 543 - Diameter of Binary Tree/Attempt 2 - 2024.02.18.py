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
        Tree
        Create dia_max var.
        Create recursive helper function to calculate heights of any given node, and update dia_max.
        We'll update dia_max after recursing both left and right with the sum of the two paths.
        Time: O(n)
        Space: O(n)
        Edge: Could be just 1 node.
        '''

        dia_max = [0]
        def recurse_tree(node):
            if not node:
                return -1
            left_h = recurse_tree(node.left)
            right_h = recurse_tree(node.right)
            cur_dia = left_h + right_h + 2
            dia_max[0] = max(dia_max[0], cur_dia)
            return 1 + max(left_h, right_h)
        recurse_tree(root)
        return dia_max[0]

