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
        Binary Tree Traverse with DFS.
        We'll return upwards the number of good nodes.
        We need to pass down the max_val of all the parents. If cur.val >= max_val, then return +1 up the stack. But
        it also needs to include the values from the children.
        We'll need a helper function so we can pass both a node and max_val.
        Create dfs(node, max_val) function.
            Base Case 1: If not node, return 0.
            good_count = 1 if (node.val >= max_val) else 0.
            Recurse node.left, add to good_count
            Recurse node.right, add to good_count
            Return good_count
        Return dfs(root, root.val)
        Time: O(n)
        Space: O(h)
        Edge: None
        '''
        def dfs(node, max_val):
            if not node:
                return 0
            good_count = 1 if (node.val >= max_val) else 0
            max_val = max(max_val, node.val)
            left_good_count = dfs(node.left, max_val)
            right_good_count = dfs(node.right, max_val)
            return (good_count + left_good_count + right_good_count)
        return dfs(root, root.val)



