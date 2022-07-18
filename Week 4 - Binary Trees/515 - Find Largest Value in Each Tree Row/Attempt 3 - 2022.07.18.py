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
        1. Create max_value_dict. Keys: Tree level,Values: max value in level.
        2. Recursively go through the LL with DFS and construct the max_value_dict.
        3. Loop through max_value_dict, construct and return the final array.
        '''

        max_value_dict = {}
        max_value_dict["counter"] = -1
        current = root

        def helper(current, max_value_dict, level):
            if not current:
                return max_value_dict
            if level not in max_value_dict:
                max_value_dict[level] = current.val
                max_value_dict["counter"] += 1
            elif max_value_dict[level] < current.val:
                max_value_dict[level] = current.val

            if current.right:
                max_value_dict = helper(current.right, max_value_dict, level+1)

            if current.left:
                max_value_dict = helper(current.left, max_value_dict, level+1)

            return max_value_dict

        max_value_dict = helper(current, max_value_dict, 0)

        final_arr = []

        for i in range(max_value_dict.get("counter")+1):
            final_arr.append(max_value_dict[i])

        return final_arr
