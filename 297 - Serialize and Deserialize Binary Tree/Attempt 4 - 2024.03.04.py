# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    297 - Serialize and Deserialize Binary Tree

    https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
    stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in
    the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
    serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized
    to a string and this string can be deserialized to the original tree structure.

    Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not
    necessarily need to follow this format, so please be creative and come up with different approaches yourself.

    Example 1:
    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]

    Example 2:
    Input: root = []
    Output: []

    Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    -1000 <= Node.val <= 1000
    '''

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        Plan:
        Tree Traversal with DFS
        Create serialized_str = []
        Create dfs(node) function. Returns None.
            Base Case 1: If not node, append "N" to serialized_str, and return
            Append node.val to serialized_str.
            Recursive Case 1: dfs(node.left)
            Recursive Case 2: dfs(node.right)
            Return None
        Call dfs(root)
        Return joined serialized_str
        Time: O(n)
        Space: O(h)
        Edge: Could be 0 nodes in root
        """
        serialized_str = []

        def dfs(node):
            if not node:
                serialized_str.append("N")
                return
            serialized_str.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(serialized_str)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        Plan:
        Tree Traversal with DFS preorder
        Convert data into an array
        Create self.i
        Create dfs() function, returns a node.
            if self.i >= len(arr): return None
            if arr[self.i] = "N": self.i++, return None
            root = TreeNode(arr[self.i])
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        Return dfs()
        Time: O(n)
        Space: O(h)
        Edge: Could be 0 nodes in data
        """
        arr = data.split(',')
        self.i = 0
        def dfs():
            # if self.i >= len(arr): return None
            if arr[self.i] == "N":
                self.i += 1
                return None
            root = TreeNode(int(arr[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()





# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))