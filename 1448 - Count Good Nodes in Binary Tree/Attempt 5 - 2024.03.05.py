# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        1448 - Count Good Nodes in Binary Tree

        https://leetcode.com/problems/count-good-nodes-in-binary-tree/

        Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no
        nodes with a value greater than X.

        Return the number of good nodes in the binary tree.

        Example 1:
        Input: root = [3,1,4,3,null,1,5]
        Output: 4
        Explanation: Nodes in blue are good.
        Root Node (3) is always a good node.
        Node 4 -> (3,4) is the maximum value in the path starting from the root.
        Node 5 -> (3,4,5) is the maximum value in the path
        Node 3 -> (3,1,3) is the maximum value in the path.

        Example 2:
        Input: root = [3,3,null,4,2]
        Output: 3
        Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

        Example 3:
        Input: root = [1]
        Output: 1
        Explanation: Root is considered as good.

        Constraints:
        The number of nodes in the binary tree is in the range [1, 10^5].
        Each node's value is between [-10^4, 10^4].

        Plan:
        Tree Traversal with DFS
        Create dfs(node, max_val) function. Returns the sum of good nodes under node, inclusive of node.
            Base Case 1: If not node, return 0
            Work 1: cur_sum = 1 if (node.val >= max_val) else 0
            Work 2: new_max_val = max(max_val, node.val)
            Recursive Case 1: left_sum = dfs(node.left, new_max_val)
            Recursive Case 2: right_sum = dfs(node.right, new_max_val)
            return cur_sum + left_sum + right_sum
        Return dfs(node, node.val)
        Time: O(n)
        Space: O(h)
        Edge: None
        '''
        def dfs(node, max_val):
            if not node: return 0
            cur_sum = 1 if (node.val >= max_val) else 0
            max_val = max(max_val, node.val)
            left_sum = dfs(node.left, max_val)
            right_sum = dfs(node.right, max_val)
            return cur_sum + left_sum + right_sum
        return dfs(root, root.val)

