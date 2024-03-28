# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        110 - Balanced Binary Tree

        https://leetcode.com/problems/balanced-binary-tree/

        Given a binary tree, determine if it is height-balanced.

        For this problem, a height-balanced binary tree is defined as:
        a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

        Input: root = [3,9,20,null,null,15,7]
        Output: true

        Input: root = [1,2,2,3,3,null,null,4,4]
        Output: false

        Input: root = []
        Output: true

        Constraints:
        The number of nodes in the tree is in the range [0, 5000].
        -10^4 <= Node.val <= 10^4

        Plan:
        Tree Traversal with DFS
        Time: O(n)
        Space: O(h)
        Edge: Could be no nodes in the tree.
        '''
        def dfs(node):
            if not node: return [True, 0]
            left_bool, left_height = dfs(node.left)
            right_bool, right_height = dfs(node.right)
            if left_bool and right_bool and (abs(left_height - right_height) <= 1):
                return [True, 1 + max(left_height, right_height)]
            else:
                return [False, 0]
        return dfs(root)[0]
