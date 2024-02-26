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
        Pass down the running min and max values. When we branch left, we need to verify that the cur.val is < parent.
        max_val. When we branch right, we need to verify that cur.val is > parent < max. If one of those breaks,
        return False. If there is no node, then return True.
        Create dfs(node, cur_min, cur_max) function. Returns bool.
            if not node: return True
            if node.val > cur_max: return False
            if node.val < cur_min: return False
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            left_bool = dfs(node.left, cur_min, node.val)
            right_bool = dfs(node.right, node.val, cur_max)
            return (left_bool and right_bool)
        Return dfs(root, float('inf'), float('-inf')).
        '''
        def dfs(node, lower_bound, upper_bound):
            if not node: return True
            if node.val >= upper_bound: return False
            if node.val <= lower_bound: return False
            left_bool = dfs(node.left, lower_bound, node.val)
            right_bool = dfs(node.right, node.val, upper_bound)
            return (left_bool and right_bool)
        return dfs(root, float('-inf'), float('inf'))

