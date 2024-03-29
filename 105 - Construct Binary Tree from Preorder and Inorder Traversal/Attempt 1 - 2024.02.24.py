# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        105 - Construct Binary Tree from Preorder and Inorder Traversal

        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

        Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
        inorder is the inorder traversal of the same tree, construct and return the binary tree.

        Example 1:
        Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        Output: [3,9,20,null,null,15,7]

        Example 2:
        Input: preorder = [-1], inorder = [-1]
        Output: [-1]

        Constraints:
        1 <= preorder.length <= 3000
        inorder.length == preorder.length
        -3000 <= preorder[i], inorder[i] <= 3000
        preorder and inorder consist of unique values.
        Each value of inorder also appears in preorder.
        preorder is guaranteed to be the preorder traversal of the tree.
        inorder is guaranteed to be the inorder traversal of the tree.
        '''
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

    # The above solution is O(n^2) time and O(n) space. Below is an O(n) time (amortized) and O(h) space solution.
    # class Solution:
    #     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #         if not preorder or not inorder:
    #             return None
    #         inorderMap = {}
    #         for i in range(len(inorder)):
    #             inorderMap[inorder[i]] = i
    #
    #         def helper(l, r):
    #             if l > r:
    #                 return None
    #             root = TreeNode(preorder.pop(0))
    #             mid = inorderMap[root.val]
    #             root.left = helper(l, mid - 1)
    #             root.right = helper(mid + 1, r)
    #             return root
    #
    #         root = helper(0, len(inorder) - 1)
    #         return root
