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
        1. Create the tree by binary searching the arrea.
        2. Calculate mid index, make that the root. root.left will be the node from left to mid-1, root.right will be
        the node from mid+1 to right. Recursively fill up the tree. If left > right, then return None.
        3. Return the initial root
        '''
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, left, right):
        if left > right:
            return None

        mid = (left+right) // 2

        node = TreeNode(nums[mid])
        node.left = self.helper(nums, left, mid-1)
        node.right = self.helper(nums, mid+1, right)
        return node

