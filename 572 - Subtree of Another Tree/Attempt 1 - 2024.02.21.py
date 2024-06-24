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
        Recursive Tree
        Create verify_mirror(cur, subroot)
            Base case 1: If there's not subroot, return True.
            Base case 2: If there's subroot and not cur, return False
            Base case 3: If cur.val != subroot.val, return False.
            left_result = verify_mirror(cur.left, subRoot.left)
            right_result = recurseTree(cur.right, subRoot.right)
            if left_result and right_result:
                Return True
            Else
                Return False

        Create recurse_tree(node):
            left_result = recurse_tree(node.left)
            right_result = recurse_tree(node.right)
            is_subtree = verify_mirror(node, subRoot)
            if is_subtree and left_result and right_result:
                return True
            else:
                return False

        Call recurse_tree(root), set to result
        Return result
        Time: O(m * n), where m = len(root), and n = len(subRoot)
        Space: O(h)
        Edge: None
        '''
        if not subRoot: return True
        if not root: return False

        def isMirror(node, sub):
            if not node and not sub:
                return True
            if node and sub and node.val == sub.val:
                return isMirror(node.left, sub.left) and isMirror(node.right,sub.right)
            else:
                return False

        return isMirror(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
