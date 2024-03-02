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

        Plan:
        Construct inorder_dict. Keys: Values in inorder, Values: Indicies associated with values.
        Create dfs(l, r) function. Return a node.
            Base Case: if l > r, then for some reason we return None.
            Create the root's Treenode, which will always be in preorder[0]. Pop the zero index to maintain this
            status for future recursions.
            Determine the root's index in the inorder_dict. This will be our mid val. All values to the left of mid
            will be on the left side of the root, while all of the values to the right of mid will be on the right
            side of the root.
            So recurse left with dfs(l, mid -1), and set equal to root.left.
            And recruse right with dfs(mid + 1, r), and set equal to root.right
            After we've fleshed out the node, return the root.
        Return dfs(0, len(inorder)-1).
        Time: O(n) amoritized with the pop(0)
        Space: O(h)
        Edge: Could be
        '''
        import collections
        inorder_dict = collections.defaultdict(int)
        for i, val in enumerate(inorder):
            inorder_dict[val] = i
        def dfs(l, r):
            if l > r: return None
            root = TreeNode(preorder.pop(0))
            mid = inorder_dict[root.val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        root = dfs(0, len(inorder)-1)
        return root
