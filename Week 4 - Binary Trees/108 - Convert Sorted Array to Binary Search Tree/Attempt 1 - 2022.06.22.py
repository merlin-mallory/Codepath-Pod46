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

        # Attempt 4: Optimal solution
        # Time: O(n)
        # Space: O(n)
        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node

        return convert(0, len(nums) - 1)


        # Attempt 3: Also works, but does not create a balanced binary tree

        # if not nums:
        #     return None
        #
        # mid = (len(nums) - 1)//2
        #
        # root = TreeNode(nums[mid])
        # root.left = self.sortedArrayToBST(nums[:mid])
        # root.right = self.sortedArrayToBST(nums[mid:])
        #
        # return root


        # Attempt 2: It looks like I'm making valid trees per the specifications, but Leetcode wants me to construct
        # full balanced trees.

        # middle_index = len(nums) // 2
        #
        # root = TreeNode(nums[middle_index])
        # dummy_node = TreeNode(-1)
        # dummy_node.right = root
        #
        # right_pointer = middle_index + 1
        # left_pointer = middle_index - 1
        #
        # while right_pointer <= len(nums)-1:
        #     root.right = TreeNode(nums[right_pointer])
        #     root = root.right
        #     right_pointer += 1
        # # if right_pointer != middle_index:
        # #     root.right = TreeNode(nums[right_pointer])
        #
        # root = dummy_node.right
        #
        # while left_pointer >= 0:
        #     root.left = TreeNode(nums[left_pointer])
        #     root = root.left
        #     left_pointer -= 1
        # # if left_pointer != middle_index:
        # #     root.left = TreeNode(nums[left_pointer])
        #
        # return dummy_node.right


        # Attempt 1
        # middle_index = (len(nums) // 2)
        #
        # right_construct = TreeNode(nums[middle_index])
        #
        # dummy_head = TreeNode(-1)
        # dummy_head.right = right_construct
        #
        # if (middle_index + 1) < len(nums)-1:
        #     # Construct the right side of the tree
        #     for i in range(middle_index+1, len(nums)-1):
        #         right_construct.right = TreeNode(nums[i])
        #         if i < len(nums)-1:
        #             right_construct = right_construct.right
        #
        # left_construct = TreeNode(nums[middle_index])
        # left_construct_pointer = TreeNode(-1)
        # left_construct_pointer.left = left_construct
        #
        # # Construct the left side of the tree
        # if (middle_index - 1) >= 0:
        #     for j in range(middle_index-1, -1, -1):
        #         left_construct.left = TreeNode(nums[j])
        #         if j < 0:
        #             left_construct = left_construct.left
        #
        # # Merge the two branches into the root
        #
        # dummy_head.right.left = left_construct_pointer.left.left
        #
        # return dummy_head.right
