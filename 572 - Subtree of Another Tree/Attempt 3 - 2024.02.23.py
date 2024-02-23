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
        Base Case 1: If there's root and not subRoot, then return True.
        Base Case 2: If there's subRoot and not Root, then return False.
        Create isMatch(root, subRoot) function. Returns a boolean regarding truthiness.
            Base Case 1: If there's not root and not subRoot, then return True.
            Base Case 2: If there's root and not subRoot, then return False.
            Base Case 3: If there's not root and subRoot, then return False
            Base Case 4. If root.val != subRoot.val, then return False
            left_bool = isMatch(root.left, subRoot.left)
            right_bool = isMatch(root.right, subRoot.right)
            Return (left_bool and right_bool)
        Return isMatch(root, subRoot) or isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
        Time: O(n*m)
        Space: O(h)
        Edge: Could only be one node.
        '''
        if root and not subRoot: return True
        if subRoot and not root: return False
        def isMatch(root, subRoot):
            if (not root) and (not subRoot): return True
            if (root and (not subRoot)) or ((not root) and subRoot): return False
            if root.val != subRoot.val: return False
            left_bool = isMatch(root.left, subRoot.left)
            right_bool = isMatch(root.right, subRoot.right)
            return (left_bool and right_bool)
        return isMatch(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
