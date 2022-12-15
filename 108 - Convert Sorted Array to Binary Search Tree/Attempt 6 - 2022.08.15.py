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
        1. Looks like we need to construct the tree recursively.
        2. Calculate the mid, make that the root. Left child is mid // 2, right child is (mid+right) // 2
        '''
        # Failed attempt. I was close, but the base case was that if left > right, not if one of those pointers goes
        # out of bounds.

        def helper(left, right):
            if left < 0 or right > len(nums)-1:
                return None

            mid = (left+right) // 2
            current = TreeNode(nums[mid])
            current.left = helper(left, mid-1)
            current.right = helper(mid+1, right)
            return current

        return helper(0, len(nums)-1)
