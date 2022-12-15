# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        https://leetcode.com/problems/binary-tree-pruning/description/
        Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a
        1 has been removed. A subtree of a node 'node' is 'node' plus every node that is a descendant of node.

        Input: root = [1,null,0,0,1]
        Output: [1,null,0,null,1]
        Explanation:
        Only the red nodes satisfy the property "every subtree not containing a 1".
        The diagram on the right represents the answer.

        Input: root = [1,0,1,0,0,0,1]
        Output: [1,null,1,null,1]

        Input: root = [1,1,0,1,1,0,1,0]
        Output: [1,1,0,1,1,null,1]

        Constraints:
        The number of nodes in the tree is in the range [1, 200].
        Node.val is either 0 or 1.

        Plan:
        1. DFS post-order traverse the tree, deleteing nodes that contain zero from the bottom of the tree towards
        the top.
        2. Return the resultant tree
        '''
        current_node = root

        def helper(current_node):
            if current_node.left:
                current_node.left = helper(current_node.left)
            if current_node.right:
                current_node.right = helper(current_node.right)
            if current_node.val != 1 and current_node.left is None and current_node.right is None:
                current_node = None
            return current_node

        return helper(root)
