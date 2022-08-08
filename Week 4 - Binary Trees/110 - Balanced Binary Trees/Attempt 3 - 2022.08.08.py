# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        https://leetcode.com/problems/balanced-binary-tree/
        Given a binary tree, determine if it is height-balanced.

        For this problem, a height-balanced binary tree is defined as:
        a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

        Input: root = [3,9,20,null,null,15,7]
        Output: true

        Input: root = [1,2,2,3,3,null,null,4,4]
        Output: false

        Input: root = []
        Output: true

        Constraints:

        The number of nodes in the tree is in the range [0, 5000].
        -10^4 <= Node.val <= 10^4

        Plan:
        1. Make a calculate_length function, which takes a node, and calculates the height of the left child and the
        height of the right child. If the absolute difference between the two ever exceeds 1, then return False.
        Otherwise, return True.
        2. Time: O(n), Space: O(1)
        '''
        # Failed Attempt. I couldn't construct the calculate_height function properly. If there's no root,
        # return -1. Otherwise return 1+max of calculate_height(left) and calculate_height(right). When there's no
        # root, the 1+ -1 will equalize to zero, to show the node doesn't exist. And then it's only in the main
        # function that I should check for height differential >1, and the left child being unbalanced, and the right
        # child being unbalanced. If we pass all three checks, then we return True, otherwise we return False.
        if not root:
            return True

        def calculate_height(node, current_height):
            if not node:
                return 0

            if node.left:
                left_count = 1 + calculate_height(node.left, current_height+1)
            else:
                left_count = 0

            if node.right:
                right_count = calculate_height(node.right, current_height+1)
            else:
                right_count = 0

            return

        return abs(calculate_height(root.left,0) - calculate_height(root.right,0)) <= 1
