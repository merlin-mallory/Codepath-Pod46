# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        102 - Binary Tree Level Order Traversal

        https://leetcode.com/problems/binary-tree-level-order-traversal/

        Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to
        right, level by level).

        Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]

        Example 2:
        Input: root = [1]
        Output: [[1]]

        Example 3:
        Input: root = []
        Output: []

        Constraints:
        The number of nodes in the tree is in the range [0, 2000].
        -1000 <= Node.val <= 1000

        Plan:
        Tree traversal BFS
        Create deque, init with root.
        Create final_arr.
        Loop while deque.
            Calc deque_len.
            cur_lvl = []
            Loop in range deque_len.
                Popleft from deque, append node.val to cur_lvl.
                If there's node.left, append node.left to deque.
                If there's node.right, append node.right to the deque
            Append cur_lvl to final_arr
        Return final_arr
        Time: O(n)
        Space: O(n)
        Edge: Could be 0 nodes in root.
        '''
        if not root: return []
        import collections
        deque = collections.deque([root])
        final_arr = []
        while deque:
            deque_len = len(deque)
            cur_lvl = []
            for _ in range(deque_len):
                cur = deque.popleft()
                cur_lvl.append(cur.val)
                if cur.left: deque.append(cur.left)
                if cur.right: deque.append(cur.right)
            final_arr.append(cur_lvl)
        return final_arr
