# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        124 - Binary Tree Maximum Path Sum

        https://leetcode.com/problems/binary-tree-maximum-path-sum/

        A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
        connecting them. A node can only appear in the sequence at most once. Note that the path does not need to
        pass through the root.

        The path sum of a path is the sum of the node's values in the path.

        Given the root of a binary tree, return the maximum path sum of any non-empty path.

        Example 1:
        Input: root = [1,2,3]
        Output: 6
        Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

        Example 2:
        Input: root = [-10,9,20,null,null,15,7]
        Output: 42
        Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

        Constraints:
        The number of nodes in the tree is in the range [1, 3 * 10^4].
        -1000 <= Node.val <= 1000

        Plan:
        Tree Traversal with DFS
        Create max_dia = [0] outside of the helper function
        Create dfs(node)
            Base Case 1: If not node: Return -1
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)
            cur_dia = left_sum + right_sum + node.val
            max_dia[0] = max(max_dia[0], cur_dia)
            return node.val + max(left_sum, right_sum)
        Call dfs(root)
        return max_dia
        '''
        max_dia = [root.val]
        def dfs(node):
            if not node: return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)
            cur_dia = left_sum + right_sum + node.val
            max_dia[0] = max(max_dia[0], cur_dia)
            return node.val + max(left_sum, right_sum)
        dfs(root)
        return max_dia[0]
