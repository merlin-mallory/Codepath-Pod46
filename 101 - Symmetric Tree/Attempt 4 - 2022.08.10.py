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
        1. There are two conditions that must be verified in order for it to be symmetric. First of all, the values
        on both sides need to match, and second of all, the number of children on both sides needs to match.
        2. So we can recursively explore both halves of the tree, and at each step check if the values and children
        match.
        3. Time: O(n), Space: O(1)
        '''
        # Failed attempt. I was on the right track with exploring both sides. But I should've done the initial call
        # with two copies of the root. The first copy will simulate node1 and the second copy will simulate
        # node2. In the helper function, the base cases are: 1. If both node1 and node2 are None,
        # then return True. 2. If either node1 or node2 are None, then return False (this would be an imbalance). 3.
        # If node1.val != node2.val, then return False (this is the easiest one to get). Then explore_left and
        # explore_right, which are recursive helper calls. explore_left is passed (node1.right, node2.left),
        # while explore_right is passed (node1.left, node2.right). Finally, if both explore1 and explore2 are True,
        # then return True, otherwise return False.

        def helper(explore_left, explore_right):
            if explore_left.val != explore_right.val:
                return False

            if explore_left.left and not explore_right.right:
                return False

            if explore_left.right and not explore_right.left:
                return False

            if explore_right.left and not explore_left.right:
                return False

            if explore_right.right and not explore_left.left:
                return False

            if self.isSymmetric(explore_left) is False:
                return False

            if self.isSymmetric(explore_right) is False:
                return False

            return True

        explore_left = root.left
        explore_right = root.right

        return helper(explore_left, explore_right)
