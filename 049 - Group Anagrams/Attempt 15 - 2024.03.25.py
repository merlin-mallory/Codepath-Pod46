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
        Hashmap
        Create hashmap
        Loop through strs
            sort cur_str, set to sorted_cur_str.
            Append cur_str to hashmap[sorted_cur_str]
        Return hashmap.values()
        Time: O(n * k log k), where n = length of strs, and k = max len of strs[i]
        Space: O(n * k)
        Edge: None
        '''
        import collections
        hashmap = collections.defaultdict(list)
        for cur_str in strs:
            sorted_cur_str = tuple(sorted(list(cur_str)))
            hashmap[sorted_cur_str].append(cur_str)
        return hashmap.values()
