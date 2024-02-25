class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        https://leetcode.com/problems/group-anagrams/

        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
        using all the original letters exactly once.

        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        Input: strs = [""]
        Output: [[""]]

        Input: strs = ["a"]
        Output: [["a"]]

        Constraints:

        1 <= strs.length <= 10^4
        0 <= strs[i].length <= 100
        strs[i] consists of lowercase English letters.

        Plan:
        Array and Hashmap
        Create dict. Keys: sorted strings, Values: List of unsorted strings grouped underneath the sorted string.
        Loop through strs.
            Sort the cur_str, convert to tuple.
            Append the cur_str to dict[sorted_str].
        Return dict.values()
        Time: O(n)
        Space: O(n)
        Edge: Could be nothing in strs.
        '''
        if len(strs) == 0: return []
        import collections
        dict = collections.defaultdict(list)
        for cur_str in strs:
            tup_str = tuple(sorted(list(cur_str)))
            dict[tup_str].append(cur_str)
        return dict.values()
