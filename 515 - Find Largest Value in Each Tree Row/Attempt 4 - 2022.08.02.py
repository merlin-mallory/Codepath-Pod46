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
        1. Make a hashmap. Keys: Row number, values: maximum value in that row.
        2. Explore the entire tree with DFS. Update the hashmap with the maximum value at each level.
        3. Return hashmap.values()
        '''
        if not root:
            return None

        hashmap = {}  # Keys: row level, value: maximum value in the key's row

        current_node = root
        level = 1

        def helper(current_node, hashmap, level):
            if level not in hashmap:
                hashmap[level] = current_node.val
            elif current_node.val > hashmap.get(level):
                hashmap[level] = current_node.val

            if current_node.left:
                hashmap = helper(current_node.left, hashmap, level+1)

            if current_node.right:
                hashmap = helper(current_node.right, hashmap, level+1)
            return hashmap

        final_dict = helper(current_node, hashmap, level)
        return final_dict.values()
