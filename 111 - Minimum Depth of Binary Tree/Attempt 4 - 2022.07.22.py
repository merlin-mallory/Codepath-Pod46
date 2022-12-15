# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
        https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
        Given a binary tree, find its minimum depth.

        The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf
        node. Note: A leaf is a node with no children.

        Input: root = [3,9,20,null,null,15,7]
        Output: 2

        Input: root = [2,null,3,null,4,null,5,null,6]
        Output: 5

        Constraints:
        The number of nodes in the tree is in the range [0, 105].
        -1000 <= Node.val <= 1000

        Plan:
        1. We will do BFS with a queue, and keep track of each node's level. Eventually we will discover a leaf node,
        the minimum depth will be the height of that first leaf node. We'll return that value.
        2. We also need to account for a tree with no nodes, that should return either 0 or None.
        '''

        if not root:
            return 0

        import collections
        queue = collections.deque()
        queue.append([root, 1])
        while queue:
            result = queue.popleft()
            current_node = result[0]
            current_height = result[1]
            if current_node.left is None and current_node.right is None:
                return current_height
            if current_node.left:
                queue.append([current_node.left, current_height+1])
            if current_node.right:
                queue.append([current_node.right, current_height+1])
