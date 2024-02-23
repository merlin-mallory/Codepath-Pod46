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
        Recursive Tree
        Init max_dia = [0] outside of dfs.
        Create dfs function. Takes node, returns a height.
            Base Case 1: If there isn't a node, then return -1.
            Recursive Case 1: Call dfs(node.left), set equal to left_height.
            Recursive Case 2: Call dfs(node.right, set equal to right_height.
            Calc cur_diameter, which is left_height + right_height + 2.
            Calc cur_height, which is max(left_height, right_height) + 1.
            return cur_height
        Call dfs(root), set equal to result.
        return result.
        Time: O(n)
        Space: O(n) to O(log(n)), depending upon the structure of the tree.
        Edge: None
        '''
        max_dia = [0]
        def dfs(node):
            if not node: return -1
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            cur_diameter = left_height + right_height + 2
            max_dia[0] = max(max_dia[0], cur_diameter)
            cur_height = max(left_height, right_height) + 1
            return cur_height
        dfs(root)
        return max_dia[0]

