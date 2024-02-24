# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        098 - Validate Binary Search Tree

        https://leetcode.com/problems/validate-binary-search-tree/

        Given the root of a binary tree, determine if it is a valid binary search tree (BST).

        A valid BST is defined as follows:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.

        Example 1:
        Input: root = [2,1,3]
        Output: true

        Example 2:
        Input: root = [5,1,4,null,null,3,6]
        Output: false
        Explanation: The root node's value is 5 but its right child's value is 4.

        Constraints:
        The number of nodes in the tree is in the range [1, 10^4].
        -2^31 <= Node.val <= 2^31 - 1

        Tree Recursion with DFS
        Base Case 1: if not node, return True.
        Base Case 2: if node.left and node.left.val >= node.val, return False.
        Base Case 3: if node.right and node.right.val <= node.val, return False.
        Recurse left
        Recurse right
        return (left_bool and right_bool)
        Time: O(n)
        Space: O(h)
        Edge: Could be only one node in root
        '''
        def dfs(node, low=float('-inf'), high=float('inf')):
            if not node: return True
            val = node.val
            if (val <= low) or (val >= high): return False
            if not dfs(node.right, val, high): return False
            if not dfs(node.left, low, val): return False
            return True
        return dfs(root)
