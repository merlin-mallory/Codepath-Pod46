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

        Plan 1:
        1. We will do an in-order traversal the tree, keeping track of the parent's location and direction of the child.
           whenever we encounter a 0, we will set parent.direction to None.
        2. Time complexity: In-order traversal is O(n) time complexity, because we need to explore every node,
        and do O(1) work on each node.
        3. Space complexity: We are not creating any additional data structures, so the space complexity will equal
        the maximum size of the recursive call stack, which would be O(n) in a linear tree, or O(log n) in a balanced
        tree.

        Plan 2:
        1. We do a recursive post-order traversal of the tree. If the node's value equals zero and the node has no
        children, then we will prune the node. The post order traversal will ensure that we prune the children before we
        consider pruning the parent.
        '''

        if root is None:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if (root.val == 0) and (root.left is None) and (root.right is None):
            root = None

        return root

