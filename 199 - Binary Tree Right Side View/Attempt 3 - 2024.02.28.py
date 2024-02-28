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
        Create stack, init with root.
        Create final_arr.
        Loop while stack.
            Calc stack_len = len(stack).
            Loop in range stack_len.
                cur_node = stack.pop()
                if i == stack_len - 1, then append cur_node.val to final_arr.
                if cur_node.left, then append it to the stack.
                if cur_node.right, then append it to the stack.
        Return final_arr.
        Time: O(n)
        Space: O(h)
        Edge: Could be 0 nodes in root.
        '''
        import collections
        if not root: return []
        deque = collections.deque([root])
        final_arr = []
        while deque:
            deque_len = len(deque)
            for i in range(deque_len):
                cur_node = deque.popleft()
                if i == deque_len - 1: final_arr.append(cur_node.val)
                if cur_node.left: deque.append(cur_node.left)
                if cur_node.right: deque.append(cur_node.right)
        return final_arr
