# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''
        https://leetcode.com/problems/find-largest-value-in-each-tree-row/
        Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

        Input: root = [1,3,2,5,3,null,9]
        Output: [1,3,9]

        Input: root = [1,2,3]
        Output: [1,3]

        Constraints:
        The number of nodes in the tree will be in the range [0, 104].
        -231 <= Node.val <= 231 - 1

        Understand: We need to return an array that contains the maximum value per row.

        Match:
        1. We could do DFS with dictionaries. Do pre-order traversal with a layer_counter, and construct a dictionary
        that contains a list of all the values in that layer. Then loop through the keys, and append the maximum
        element in each layer to the final array. Time complexity: O(n) to construct the dictionary, O(n) to loop
        through all the entries the dictionary to find the max at each layer, final O(n). Space complexity: We will
        be making a O(z) size dictionary, where z is the number of layers in the binary tree. A full balanced binary
        tree will require O(log(n)) space, however a linear binary tree will require O(n) additional space.
        2. We could do BFS with queues. Enqueue the root, pop the root until empty, add the children. Add the max
        element in the queue to final array, record the length of the array, enqueue the children's children,
        pop the length of the array, so the array will contain the next layer. Loop until the queue is empty.
        '''
        # Edge Cases
        if not root:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        def helper(root, layer_dict, layer_counter):
            if root is None:
                return layer_dict

            if layer_counter not in layer_dict:
                layer_dict[layer_counter] = root.val
            else:
                layer_dict[layer_counter] = max(layer_dict[layer_counter], root.val)

            if root.left:
                layer_dict = helper(root.left, layer_dict, layer_counter + 1)

            if root.right:
                layer_dict = helper(root.right, layer_dict, layer_counter + 1)

            return layer_dict

        # Initialization
        layer_counter = 0
        layer_dict = {0: root.val}

        # Construct the dictionary of max values
        if root.left:
            layer_dict = helper(root.left, layer_dict, layer_counter + 1)
        if root.right:
            layer_dict = helper(root.right, layer_dict, layer_counter + 1)

        # Loop through the dictionary of max values, and return the max set
        result_list = []
        for key in layer_dict:
            result_list.append(layer_dict[key])
        return result_list
