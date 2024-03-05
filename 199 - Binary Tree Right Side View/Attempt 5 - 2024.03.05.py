# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        199 - Binary Tree Right Side View

        https://leetcode.com/problems/binary-tree-right-side-view/

        Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the
        nodes you can see ordered from top to bottom.

        Example 1:
        Input: root = [1,2,3,null,5,null,4]
        Output: [1,3,4]

        Example 2:
        Input: root = [1,null,3]
        Output: [1,3]

        Example 3:
        Input: root = []
        Output: []

        Constraints:
        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100

        Plan:
        Tree Traversal with BFS
        Create deque, init with root.
        Create final_arr.
        Loop while deque.
            cur = deque.popleft()
            Calc the deque's length.
            Loop in range(deque_len).
                if i == (deque_len - 1): append cur.val to final_arr
                if cur.left: append cur.left to deque.
                if cur.right: append cur.right to deque
        return final_arr.
        Time: O(n)
        Space: O(n)
        Edge: Could be 0 nodes in the tree.
        '''
        if not root: return []
        import collections
        deque = collections.deque([root])
        final_arr = []
        while deque:
            deque_len = len(deque)
            for i in range(deque_len):
                cur = deque.popleft()
                if i == (deque_len - 1): final_arr.append(cur.val)
                if cur.left: deque.append(cur.left)
                if cur.right: deque.append(cur.right)
        return final_arr
