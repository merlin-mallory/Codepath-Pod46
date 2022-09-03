# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''
        https://leetcode.com/problems/find-largest-value-in-each-tree-row/
        Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

        Input: root = [1,3,2,5,3,null,9]
        Output: [1,3,9]

        Input: root = [1,2,3]
        Output: [1,3]

        Constraints:
        The number of nodes in the tree will be in the range [0, 10^4].
        -2^31 <= Node.val <= 2^31 - 1

        Plan:
        1. Looks like implement BFS.
        2. Create a hashmap. Keys: Level, values: max value in that level
        3. Loop through the tree with DFS and create the hashmap
        4. Return hashmap.values()
        '''

        hashmap = {}

        def helper(node, level):
            if not node:
                return

            if level not in hashmap:
                hashmap[level] = node.val
            else:
                hashmap[level] = max(node.val, hashmap.get(level))

            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)


        helper(root, 0)
        return hashmap.values()

