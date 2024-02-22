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
        If not subRoot, return True.
        If not root, return False.

        Create is_match function(root, subRoot), returns bool.
            If not root and not subRoot, return True.
            If (root and not subRoot) or (not root and subRoot), return False.
            If root.val != subRoot.val, return False.
            left_bool = is_match(root.left, subRoot.left)
            right_bool = is_match(root.right, subRoot.right)
            return (left_bool and right_bool)

        return isSubTree(root) or is_match(root.left) or is_match(root.right)
        '''
        if not subRoot: return True
        if not root: return False
        def is_match(root, subRoot):
            if (not root) and (not subRoot):
                return True
            if (root and (not subRoot)) or (subRoot and (not root)):
                return False
            if root.val != subRoot.val:
                return False
            left_bool = is_match(root.left, subRoot.left)
            right_bool = is_match(root.right, subRoot.right)
            if left_bool and right_bool:
                return True
            else:
                return False

        return (is_match(root, subRoot)) or (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))
