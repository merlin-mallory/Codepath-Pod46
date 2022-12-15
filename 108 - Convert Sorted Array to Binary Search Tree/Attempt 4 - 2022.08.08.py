# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

        Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced
        binary search tree.

        A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never
        differs by more than one.

        Input: nums = [-10,-3,0,5,9]
        Output: [0,-3,9,-10,null,5]
        Explanation: [0,-10,5,null,-3,null,9] is also accepted:

        Input: nums = [1,3]
        Output: [3,1]
        Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

        Constraints:
        1 <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        nums is sorted in a strictly increasing order.

        Plan:
        1. Calculate the mid index, and make the root.
        2. Binary search down the left and right paths to fill up the tree recursive.
        3. Return the final tree
        '''

        # Failed attempt, the generate_node base case was checking if left and right were in bounds, instead of
        # checking for left exceeding right.

        left_index = 0
        right_index = len(nums)-1
        mid_index = (left_index + right_index) // 2

        def generate_node(left_index, right_index):
            if left_index > right_index:
                return None

            mid_index = (left_index+right_index) // 2
            new_node = TreeNode(nums[mid_index])
            new_node.left = generate_node(left_index, mid_index-1)
            new_node.right = generate_node(mid_index+1, right_index)

            return new_node

        root = TreeNode(nums[mid_index])
        root.left = generate_node(left_index, mid_index-1)
        root.right = generate_node(mid_index+1, right_index)

        return root
