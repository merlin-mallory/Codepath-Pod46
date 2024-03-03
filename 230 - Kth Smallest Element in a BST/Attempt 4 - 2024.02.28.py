# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        230 - Kth Smallest Element in a BST

        https://leetcode.com/problems/kth-smallest-element-in-a-bst/

        Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all
        the values of the nodes in the tree.

        Example 1:
        Input: root = [3,1,4,null,2], k = 1
        Output: 1

        Example 2:
        Input: root = [5,3,6,2,4,null,null,1], k = 3
        Output: 3

        Constraints:
        The number of nodes in the tree is n.
        1 <= k <= n <= 10^4
        0 <= Node.val <= 10^4

        Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find
        the kth smallest frequently, how would you optimize?

        Plan:
        Tree Traversal with DFS in-order
        Create self.counter outside of helper function.
        Create dfs(node, counter) function. Returns int.
            Recurse left with dfs(node.left, counter+1)
            Counter += 1
            Check if counter == k, if so, return node.val.
            Recurse right
        Return dfs(node, 0)
        Time: O(log(n))
        Space: O(1)
        Edge: None
        '''
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            k -= 1
            if k == 0:
                return root.val

            root = root.right
