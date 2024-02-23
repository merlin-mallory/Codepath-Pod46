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
        Binary Tree traversal with BFS (deque).
        Create final_arr.
        Create deque, init with root.
        Loop while deque.
            Calc deque_len.
            Create lvl_list.
            Loop in range(deque_len).
                popleft from the deque, set to cur.
                Append cur.val to lvl_list.
                If there's cur.left, append to deque.
                If there's cur.right, append to deque.
            Append lvl_list to final_arr.
        return final_arr
        Time: O(n)
        Space: O(n)
        Edge: Could be no nodes in tree.
        '''
        if not root: return []
        import collections
        deque = collections.deque([root])
        final_arr = []
        while deque:
            deque_len = len(deque)
            lvl_list = []
            for _ in range(deque_len):
                cur = deque.popleft()
                lvl_list.append(cur.val)
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)
            final_arr.append(lvl_list)
        return final_arr