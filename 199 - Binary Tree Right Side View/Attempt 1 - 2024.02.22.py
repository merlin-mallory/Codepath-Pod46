# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        199 - Binary Tree Right Side View

        https://leetcode.com/problems/binary-tree-right-side-view/

        Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the
        nodes you can see ordered from top to bottom.

        Example 1:
        Input: root = [1,2,3,null,5,null,4]
        Output: [1,3,4]

        Example 2:
        Input: root = [1,null,3]
        Output: [1,3]

        Example 3:
        Input: root = []
        Output: []

        Constraints:
        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100

        Plan:
        Binary Tree BFS
        Create deque(init with root), final_arr.
        Loop while deque.
            cur_lvl = []
            Loop in range(len(deque))
                cur_node = deque.popleft()
                cur_lvl.append(cur_node.val)
                If cur_node.right: Append cur_node.right to deque
                If cur_node.left: Append cur_node.left to deque.
            final_arr.append(cur_lvl[-1])
        Return final_arr
        '''
        import collections
        deque = collections.deque([root])
        final_arr = []

        if not root: return []
        while deque:
            len_of_deque = len(deque)
            for i in range(len_of_deque):
                cur_node = deque.popleft()
                if i == (len_of_deque - 1):
                    final_arr.append(cur_node.val)
                if cur_node.left:
                    deque.append(cur_node.left)
                if cur_node.right:
                    deque.append(cur_node.right)
        return final_arr
