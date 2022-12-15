# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        https://leetcode.com/problems/symmetric-tree/description/
        Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

        Input: root = [1,2,2,3,4,4,3]
        Output: true

        Input: root = [1,2,2,null,3,null,3]
        Output: false

        Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        -100 <= Node.val <= 100

        Plan:
        1. A binary tree is not symmetric if the values on both halves of the tree are not the same, or if one half
        of the tree has more nodes than the other. Otherwise, it is symmetric.
        2. So we should explore both halves of the root node, and each point verify that both the value and number of
        children on both sides are equal. If we discover a mismatch at any point, then return False.
        3. If we explore the entire tree without discovering a mismatch, then we've determined that the tree is
        symmetric, so return True.
        '''
        # Failed attempt, I should do the recursive solution instead. Make is_mirror helper that takes both sides of
        # the tree. Base case 1: If both sides are None, then return True. Base case 2: If either side is None,
        # then return False. Base case 3: If left.val != right.val, then return False. Then explore both sides(
        # t1.right, t2.left) and (t1.left, t2.right). If both explorations are True, then return True. Otherwise
        # return False, because of the mismatch.

        # Alternatively, I could have done a stack implementation, and use the same base cases.

        # Failed interative attempt below
        if root.left is None and root.right is None:
            return True

        import collections
        left_queue = collections.deque([root.left])
        right_queue = collections.deque([root.right])

        while left_queue and right_queue:
            current_left_node = left_queue.popleft()
            current_right_node = right_queue.popleft()
            if (current_left_node.left.val != current_right_node.right.val) or (current_left_node.right.val !=
                                                                        current_right_node.left.val):
                return False

            if current_left_node.left and not current_right_node.right:
                return False

            if current_left_node.right and not current_right_node.left:
                return False

            if current_right_node.left and not current_left_node.right:
                return False

            if current_right_node.right and not current_left_node.left:
                return False

            if current_left_node.left:
                left_queue.append(current_left_node.left)

            if current_left_node.right:
                left_queue.append(current_left_node.right)

            if current_right_node.right:
                left_queue.append(current_right_node.right)

            if current_right_node.left:
                right_queue.append(current_right_node.left)

        if left_queue or right_queue:
            return False

        return True
