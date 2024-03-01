# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        104 Maximum Depth of Binary Tree

        https://leetcode.com/problems/maximum-depth-of-binary-tree/

        Given the root of a binary tree, return its maximum depth.

        A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the
        farthest leaf node.

        Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: 3

        Example 2:
        Input: root = [1,null,2]
        Output: 2

        Constraints:
        The number of nodes in the tree is in the range [0, 10^4].
        -100 <= Node.val <= 100

        Plan:
        Tree Recursion DFS
        Base Case 1: If not node return 0
        left_height = maxDepth(node.left)
        right_height = maxDepth(node.right
        return 1 + max(left_height, right_height)
        Time: O(n)
        Space: O(h)
        Edge: There could be 0 nodes in root.
        '''
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

