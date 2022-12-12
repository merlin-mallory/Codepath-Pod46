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
        1. Loop through strs, sort strs[i], and then add the result to a mapping_dict (keys: sorted strings,
        values: list of anagrams matching key.
        2. Return mapping_dict.values()
        '''
        if strs == [""]:
            return [[""]]
        import collections
        mapping_dict = collections.defaultdict(list)  # Keys: Sorted anagrams, Values: List of strs[i]
        for my_str in strs:
            mapping_dict[str(sorted(my_str))].append(my_str)
        final_arr = []
        for key in mapping_dict:
            final_arr.append(mapping_dict[key])
        print("final arr:", final_arr)
        return final_arr
