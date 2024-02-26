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

        Root of the tree will be at preorder[0]. If we find i=the index of that value in inorder, that will show us
        where the divide is between the two trees. Everything to the left will be under node.left, everything to the
        right will be under node.right. So set node.left = dfs(preorder[1:mid+1, inorder?
        '''
        if not preorder or not inorder: return None
        import collections
        inorder_dict = collections.defaultdict(int)
        for i, val in enumerate(inorder):
            inorder_dict[val] = i

        def dfs(l, r):
            if l > r:
                return
            root = TreeNode(preorder.pop(0))
            mid = inorder_dict[root.val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        root = dfs(0, len(inorder)-1)
        return root
