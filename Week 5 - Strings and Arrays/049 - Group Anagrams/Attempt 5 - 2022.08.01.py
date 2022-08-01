import collections


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
        1. Loop through sts, sort each individual my_str, and check if the sorted result is in my_dict. If it is in
        my_dict, then append my_str to the existing value. Otherwise, add the key and value to the dict.
        2. Loop through the dict, and append all the values to a final return array.
        '''
        import collections
        mapping_dict = {}
        for my_str in strs:
            sorted_str = str(sorted(my_str))
            if sorted_str in mapping_dict:
                mapping_dict[sorted_str].append(my_str)
            else:
                mapping_dict[sorted_str] = [my_str]

        return mapping_dict.values()
        