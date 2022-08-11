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
        1. Create anagram_dict. Keys: sorted anagram, Values: list of strings matching the sorted anagram.
        2. Loop through strs and construct anagram_dict.
        3. Return anagram_dict.values()
        '''
        import collections
        anagram_dict = collections.defaultdict(list)
        for my_str in strs:
            my_str_sorted = str(sorted(my_str))
            anagram_dict[my_str_sorted].append(my_str)
        return anagram_dict.values()
        