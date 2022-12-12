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

        1 <= strs.length <= 104
        0 <= strs[i].length <= 100
        strs[i] consists of lowercase English letters.

        Plan:
        1. Create a dictionary that will hold each unique anagram. Keys = tuple containing anagram, Values = list of
        strings that match that anagram.
        2. Loop through strs.
            3. Convert each string to a sorted list.
            4. Convert the sorted list into a tuple.
            5. Insert the str into the correct list in the dictionary.
        6. After we finish construction of the dictionary, return a list that contains all of the values.
        '''

        from collections import defaultdict
        anagram_dict = collections.defaultdict(list)

        for str in strs:
            anagram_dict[tuple(sorted(str))].append(str)
        return anagram_dict.values()


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = collections.defaultdict(list)
#
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] += 1
#             ans[tuple(count)].append(s)
#         return ans.values()