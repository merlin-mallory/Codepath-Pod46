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
        inorder is guaranteed to be the inorder traversal of the tree.\

        Plan:
        Tree Traversal with DFS
        Create inorder_dict. Keys: inorder[i], Values: i
        Create dfs() function.
            Pop the zero index from Preorder to find the value of what the next node should be.
            Use the inorder_dict to locate the mid point's index. Everything to the left should be under the left
            children, and everything to the right should be under the right child.
            Recursively attach the node.left and node.right nodes.
            Return upwards node, which will eventually become the root
        Return dfs()
        Time: O(n) amoritized
        Space: O(h)
        Edge: None
        '''
        inorder_dict = {}
        for i, val in enumerate(inorder):
            inorder_dict[val] = i
        def dfs(l, r):
            if l > r: return None
            cur_val = preorder.pop(0)
            m = inorder_dict[cur_val]
            node = TreeNode(cur_val)
            node.left = dfs(l, m-1)
            node.right = dfs(m+1, r)
            return node
        return dfs(0, len(inorder)-1)
