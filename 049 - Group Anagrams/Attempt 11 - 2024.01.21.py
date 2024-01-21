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

        1. Create hashmap. (Keys: sorted strings, Value: Array of raw strings that matched the sorted value)
        2. Loop through strs
            3. Add current_str to hashamp.
        4. Return hashmap.values()
        '''
        import collections
        hashmap = collections.defaultdict(list)

        for current_str in strs:
            sorted_str = tuple(sorted(list(current_str)))
            hashmap[sorted_str].append(current_str)

        return hashmap.values()
