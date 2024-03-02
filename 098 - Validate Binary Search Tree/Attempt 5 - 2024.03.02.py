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

        Plan:
        Tree Recursion with DFS
        Create dfs(node, left_bound, right_bound) function. Returns bool indicating binality.
            Base Case 1: If not node: Return True.
            Base Case 2: If node.val < left_bound: Return False
            Base Case 3: If node.val > right_bound: Return False
            left_bool = dfs(node.left, left_bound, node.val)
            right_bool = dfs(node.right, node.val, right_bound)
            return (left_bool and right_bool)
        Return dfs(root, float('-inf'), float('inf'))
        Time: O(n)
        Space: O(h)
        Edge: None
        '''
        def dfs(node, left_bound, right_bound):
            if not node: return True
            if node.val <= left_bound: return False
            if node.val >= right_bound: return False
            left_bool = dfs(node.left, left_bound, node.val)
            right_bool = dfs(node.right, node.val, right_bound)
            return (left_bool and right_bool)
        return dfs(root, float('-inf'), float('inf'))

