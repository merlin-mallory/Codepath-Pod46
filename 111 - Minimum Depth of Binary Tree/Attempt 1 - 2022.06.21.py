# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
        https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
        Given a binary tree, find its minimum depth.

        The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf
        node. Note: A leaf is a node with no children.

        Input: root = [3,9,20,null,null,15,7]
        Output: 2
        Example 2:

        Input: root = [2,null,3,null,4,null,5,null,6]
        Output: 5

        Constraints:
        The number of nodes in the tree is in the range [0, 105].
        -1000 <= Node.val <= 1000

        Plan 1:
        1. Make an explore_down(node, counter) function.
            2. Makes two recursive calls per node. Base case: Node is null, return depth_counter. Recursive call: One
            explores node.left, the other explores node.right. Return 1 + maximum depth counter.
        3. In minDepth, call explore_down on the root node.
        4. Handle the edge case of no node
        5. Time complexity: The worst case is a linear tree, which would have an O(n) size callstack, and O(1) work
        per node, so overall O(n) time complexity.
        6. Space complexity: Also O(n), because we didn't create any additional data structures.

        Plan 2:
        1. Make this a recursive function.
            2. Base case 1: If there is no root, then return 0.
            3. Base case 2: If there are no children, then return 1
            4. Recursive call 1: Calculate the depth of the left child.
            5. Recursive call 2: Calculate the depth of the right child.
            6. Return 1 + the minimum of recursive call 1 and recursive call 2.
        7. Time complexity: The worst case is a linear tree, which would have an O(n) size callstack, and O(1) work
        per node, so overall O(n) time complexity.
        8. Space complexity: Also O(n), because we didn't create any additional data structures.
        '''
        if not root:
            return 0

        children = [root.left, root.right]
        if not any(children):
            return 1

        min_depth = float('inf')
        for child in children:
            if child:
                min_depth = min(self.minDepth(child), min_depth)
        return min_depth + 1

        # if not root:
        #     return 0
        #
        # if root.left is None:
        #     return 1 + self.minDepth(root.right)
        # if root.right is None:
        #     return 1 + self.minDepth(root.left)
        #
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

