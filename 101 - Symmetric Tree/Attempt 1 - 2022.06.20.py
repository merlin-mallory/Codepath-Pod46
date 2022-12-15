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

        Plan1:
        1. Inverse the left child, and compare it to the right child. If they match, return True. Otherwise,
        return false. Not sure if this will work with comparison of two linked lists.

        Plan 2:
        1. Create an is_mirror function that compares two trees, t1 and t2.
            2. If both t1 and t2 are None, then return True, because nothing is a mirror image of nothing.
            3. If either t1 or t2 are None, then return False, because one subtree has more depth than the other.
            4. If t1.val and t2.val mismatch, then return False, because mirrors must have identical values.
            5. Recursive call 1: Check if t1's right is_mirror with t2's left.
            6. Recursive call 2: Check if t1's left is_mirror with t2's right.
            7. If both recursive call 1 and recursive call 2 are True, then we've verified that the current node is
            mirrored, so return True. Otherwise, return False, because it means there's some mismatch in the subtrees.
        2. Make isSymmetric call is_mirror(root, root). If the root is_mirror, then it will return True,
        otherwise return False.
        3. Time complexity: The max height of the recursive tree could be n, because there is no guarentee that we
        will have a balanced tree. And we are making 2 recursive calls per node. So the time complexity is O(2^n).
        4. Space complexity: We need O(1) space on each node, and the maximum size of the callstack will be O(n),
        so the overall space complexity will be O(n)
        '''

        return self.is_mirror(root, root)

    def is_mirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True

        if t1 is None or t2 is None:
            return False

        if t1.val != t2.val:
            return False

        explore1 = self.is_mirror(t1.right, t2.left)
        explore2 = self.is_mirror(t1.left, t2.right)

        if explore1 is True and explore2 is True:
            return True
        else:
            return False









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

        Plan1:
        1. Inverse the left child, and compare it to the right child. If they match, return True. Otherwise,
        return false. Not sure if this will work with comparison of two linked lists.

        Plan 2:
        1. Create an is_mirror function that compares two trees, t1 and t2.
            2. If both t1 and t2 are None, then return True, because nothing is a mirror image of nothing.
            3. If either t1 or t2 are None, then return False, because one subtree has more depth than the other.
            4. If t1.val and t2.val mismatch, then return False, because mirrors must have identical values.
            5. Recursive call 1: Check if t1's right is_mirror with t2's left.
            6. Recursive call 2: Check if t1's left is_mirror with t2's right.
            7. If both recursive call 1 and recursive call 2 are True, then we've verified that the current node is
            mirrored, so return True. Otherwise, return False, because it means there's some mismatch in the subtrees.
        2. Make isSymmetric call is_mirror(root, root). If the root is_mirror, then it will return True,
        otherwise return False.
        3. Time complexity: The max height of the recursive tree could be n, because there is no guarentee that we
        will have a balanced tree. However this function will immediately return False on the first node checked. So
        the worst case height of the recursive tree would actually be a perfectly balanced binary tree, which has a
        height of log(n). And we are making 2 recursive calls per node, so the overall time complexity is 2^(log(n)).
        4. Space complexity: We need O(1) space on each node, and the maximum size of the callstack will be O(n),
        so the overall space complexity will be O(n)
        '''

        return self.is_mirror(root, root)

    def is_mirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True

        if t1 is None or t2 is None:
            return False

        if t1.val != t2.val:
            return False

        explore1 = self.is_mirror(t1.right, t2.left)
        explore2 = self.is_mirror(t1.left, t2.right)

        if explore1 is True and explore2 is True:
            return True
        else:
            return False