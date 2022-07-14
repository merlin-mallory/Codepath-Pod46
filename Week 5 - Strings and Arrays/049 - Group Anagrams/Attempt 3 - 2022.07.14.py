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
        '''
        import collections

        ana_dict = collections.defaultdict(list)
        # Keys: sorted anagrams, Values: list of str[i] that share same anagram

        for string in strs:
            my_str = str(sorted(string))
            ana_dict[my_str].append(string)

        final_arr = []

        for key in ana_dict:
            final_arr.append(ana_dict.get(key))

        return final_arr
