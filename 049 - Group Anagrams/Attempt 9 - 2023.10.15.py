import collections


class Solution:
    def groupAnagrams(self, strs):
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

        1. Loop through strs
            2. sort the str, and add to dict. Creating new entry, if there was one, or appending to list, if already
            exist.
        3. Loop through the dict and construct the final array.
        '''

        from collections import defaultdict
        my_dict = collections.defaultdict(list)

        for my_string in strs:
            my_dict[tuple(sorted(my_string))].append(my_string)
            print(tuple(sorted(my_string)))

        return my_dict.values()


result = Solution()
test1 = result.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
print(test1)
