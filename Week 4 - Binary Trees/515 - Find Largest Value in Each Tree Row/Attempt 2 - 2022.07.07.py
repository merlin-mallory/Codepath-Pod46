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
        The number of nodes in the tree will be in the range [0, 104].
        -231 <= Node.val <= 231 - 1

        Plan:
        1. Create a mapping_dict that will store the maximum value of each row of the tree.
        2. Construct a mapping_dict by traversing the entire tree with BFS.
        3. Loop through the mapping_dict to construct and return the final array.
        4. Time: O(n), Space: O(n)
        '''

        if not root:
            return []

        mapping_dict = {}
        row = 1

        def helper(root, mapping_dict, row):
            if row not in mapping_dict.keys():
                mapping_dict[row] = root.val
            if root.val > mapping_dict[row]:
                mapping_dict[row] = root.val

            if root.left:
                mapping_dict = helper(root.left, mapping_dict, row+1)
            if root.right:
                mapping_dict = helper(root.right, mapping_dict, row+1)
            return mapping_dict

        final_dict = helper(root, mapping_dict, row)
        final_arr = []
        for key in final_dict:
            final_arr.append(final_dict[key])
        return final_arr
