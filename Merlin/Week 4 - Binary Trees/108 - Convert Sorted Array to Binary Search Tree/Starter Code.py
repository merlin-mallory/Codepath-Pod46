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
        1 <= nums.length <= 104
        -104 <= nums[i] <= 104
        nums is sorted in a strictly increasing order.

        Understand:
        1. We are given a sorted array, and we will make a binary search tree. The result that we return needs to be
        balanced according to height, but it does not necessarily need to be a full tree.

        Match:
        1. We will create a binary search tree.

        Plan:
        So it's possible to just
        make the middle index the root, and fill out root.left with the values left of the middle index, and fill out
        root.right with the values right of the middle index. It shouldn't matter if there's an odd or even number of
        indexes, because the heights can differ by 1. This will not be an optimal binary search tree, but it will be
        a binary search tree. There will only be a max of 10^4 nodes so it should be fine.
        '''
