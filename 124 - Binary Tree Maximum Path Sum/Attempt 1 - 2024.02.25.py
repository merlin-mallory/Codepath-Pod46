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
        Binary Tree Recursion DFS
        Create max_val array that will hold the answer in the zero-index. Init with root.val.
        Create dfs(node) function. Returns int.
            Calc the max_val of the left_child and right_child. They could potentially be negative, so also take the
            max of 0 and the value. Return up node.val + max(left_child, right_child).
        Calln dfs(root)
        Return max_sum[0]
        '''
        max_sum = [root.val]
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)
            # Calc max path sum that includes the current node and both children
            max_sum[0] = max(max_sum[0], node.val + left_sum + right_sum)
            # Return up the maximum single path sum.
            return node.val + max(left_sum, right_sum)
        dfs(root)
        return max_sum[0]
