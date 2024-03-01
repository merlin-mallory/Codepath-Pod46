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
        Tree Recursion with DFS
        Create max_dia outside of the dfs function.
        Create dfs(node) function. Returns an int indicating the maximum path inclusive of the node.
            Base Case 1: If not node, return -1
            Recursive Case 1: left_path = dfs(node.left)
            Recursive Case 2: right_path = dfs(node.right)
            Work 1: left_path = max(left_path, 0)
            Work 2: right_path = max(right_path, 0)
            Work 3: side_dia = 2 + left_path + right_path
            Work 4: max_dia = max(max_dia, side_dia)
            Return 1 + max(left_path, right_path)
        Return dfs(root).
        '''
        max_dia = [0]
        def dfs(node):
            if not node: return -1
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            # left_path = max(left_path, 0)
            # right_path = max(right_path, 0)
            side_dia = 2 + left_path + right_path
            max_dia[0] = max(max_dia[0], side_dia)
            return 1 + max(left_path, right_path)

        dfs(root)
        return max_dia[0]
