# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        572 - Subtree of Another Tree

        https://leetcode.com/problems/subtree-of-another-tree/

        Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
        structure and node values of subRoot and false otherwise.

        A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
        The tree tree could also be considered as a subtree of itself.

        Example 1:
        Input: root = [3,4,5,1,2], subRoot = [4,1,2]
        Output: true

        Example 2:
        Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
        Output: false

        Constraints:
        The number of nodes in the root tree is in the range [1, 2000].
        The number of nodes in the subRoot tree is in the range [1, 1000].
        -10^4 <= root.val <= 10^4
        -10^4 <= subRoot.val <= 10^4

        Plan:
        Tree Traversal with DFS
        Time: O(m * n), where m = len(root), and n = len(subRoot)
        Space: O(h)
        Edge: None
        '''
        if root and not subRoot: return True
        if subRoot and not root: return False
        def isSame(node1, node2):
            if (not node1) and (not node2): return True
            if node1 and (not node2): return False
            if (not node1) and node2: return False
            if node1.val != node2.val: return False
            left_bool = isSame(node1.left, node2.left)
            right_bool = isSame(node1.right, node2.right)
            if (left_bool and right_bool):
                return True
            else:
                return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or isSame(root, subRoot)
