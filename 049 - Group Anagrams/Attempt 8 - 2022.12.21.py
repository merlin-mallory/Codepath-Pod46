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

        1. Create ana_dict. Keys: unique sorted anagrams, Values: list of anagrams from strs
        2. Loop through strs, sort each string, build up ana_dict.
        3. Return ana_dict.values()
        '''
        from collections import defaultdict
        ana_dict = defaultdict(list)
        for string in strs:
            sorted_str = tuple(sorted(string))
            ana_dict[sorted_str].append(string)
        return ana_dict.values()