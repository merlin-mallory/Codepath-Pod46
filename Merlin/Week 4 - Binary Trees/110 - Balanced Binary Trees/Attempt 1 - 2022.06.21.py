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
        -104 <= Node.val <= 104

        Plan:
        1. Create a max_depth(node, counter) function. This function does a preorder traversal of the given node and
        returns the maximum depth.
        2. Call max_depth on the root's left child and right child. If the absolute value of the difference between
        the children's height is > 1, then return False. Otherwise, return True.
        3. Time Complexity: O(n*log n). The worst case is a tree that is full, except the root has a single right
        node. In this case, we need to explore every node once, and each node will call the find_height function
        O(log n) times.
        4. Space Complexity: O(n). The worst case is that the tree is skewed linearly to the left, in which case the
        recursive stack will contain all of the nodes before returning False.
        '''
        if not root:
            return True

        height_diff = abs(self.find_height(root.left) - self.find_height(root.right))
        if height_diff > 1:
            return False

        if self.isBalanced(root.left) is False:
            return False

        if self.isBalanced(root.right) is False:
            return False

        return True

    def find_height(self, root: TreeNode):
        if not root:
            return -1
        return 1 + max(self.find_height(root.left), self.find_height(root.right))


# class Solution(object):
#     def isBalanced(self, root):
#         def check(root):
#             if not root:
#                 return 0
#
#             left = check(root.left)
#             if left == -1:
#                 return -1
#             right = check(root.right)
#             if right == -1:
#                 return -1
#
#             if abs(left - right) > 1:
#                 return -1
#             return max(left, right) + 1
#
#         return check(root) != -1