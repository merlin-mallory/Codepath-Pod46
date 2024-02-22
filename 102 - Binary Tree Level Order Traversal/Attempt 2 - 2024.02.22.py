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
        Binary Tree BFS Traversal
        Create a deque, init with root
        Create a dict. Keys: Levels, Values: List of sorted values in keys.
        Loop while deque.
            cur_level = len(deque)
            cur_arr = []
            for i in range(cur_level):
                cur_node = deque.popleft()
                cur_arr.append(cur_node.val)
                if cur_node.left: append cur_node.left to deque.
                if cur_node.right: append cur_node.right to deque.
            dict[cur_level] = cur_arr
        return dict.values()
        Time: O(n)
        Space: O(log(n)) to O(n), depending upon the structure of the binary tree
        Edge: Could be no nodes
        '''
        import collections
        deque = collections.deque([root])
        final_arr = []

        if not root: return []

        while deque:
            cur_arr = []
            for _ in range(len(deque)):
                cur_node = deque.popleft()
                cur_arr.append(cur_node.val)
                if cur_node.left:
                    deque.append(cur_node.left)
                if cur_node.right:
                    deque.append(cur_node.right)
            final_arr.append(cur_arr)
        return final_arr
