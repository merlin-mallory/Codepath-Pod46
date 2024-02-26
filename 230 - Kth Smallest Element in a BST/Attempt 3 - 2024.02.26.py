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
        Tree Iteration DFS in-order
        stack = []
        cur = head
        counter = 0
        while cur:
            while cur.left:
                stack.append(cur)
                cur = cur.left
            stack.pop()

            counter += 1
            if counter == k:
                return cur.val

            while cur.right:
                stack.append(cur)
                cur = cur.right
            stack.pop()
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
