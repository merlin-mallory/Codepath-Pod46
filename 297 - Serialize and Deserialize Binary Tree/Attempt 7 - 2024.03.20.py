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
        Tree Traversal with DFS (inorder)
        Create serialzed_str array.
        Create dfs(node) function.
            Base Case 1: If not node, then append "N" to serialized_str, and return.
            dfs(node.left)
            Append node.val to serialized_str.
            dfs(node.right)
        Join and return serialized_str.
        Time: O(n)
        Space: O(h)
        Edge: Could be 0 nodes in root.
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
        return ",".join(serialized_str)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        Plan:
        Set deserialized_str = ','.split(data)
        Use a global i variable to move through the serialized string.
        self.i = 0
        Tree Construction with DFS (inorder)
            Base Case 1: if deserialized_str[self.i] == "N", self.i++, and return None
            Recursive Case 1: node.left = dfs()

            Work:
            node = TreeNode(int(deserialized_str[self.i])).
            self.i += 1

            Recursive Case 2: node.right = dfs()

            Return up the node.
        Time: O(n)
        Space: O(h)
        Edge: None
        """
        deserialzed_str = data.split(",")
        self.i = 0
        def dfs():
            if deserialzed_str[self.i] == "N":
                self.i += 1
                return
            node = TreeNode(int(deserialzed_str[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
