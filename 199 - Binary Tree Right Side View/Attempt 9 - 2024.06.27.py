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
        Time: O(n)
        Space: O(n)
        Edge: Could be 0 nodes in the tree, if that's the cast return an empty list
        '''
        import collections
        if not root: return []
        deque = collections.deque([root])
        final_arr = []
        while deque:
            deque_len = len(deque)
            for i in range(deque_len):
                node = deque.popleft()
                if i == (deque_len - 1): final_arr.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
        return final_arr