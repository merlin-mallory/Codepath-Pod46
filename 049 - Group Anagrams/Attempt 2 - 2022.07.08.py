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
        1. Create a anagram_to_val_dict. Keys: sorted anagrams, values: list of anagrams matching the sorted value.
        2. Loop through strs and fill up the dictionary
        3. Create a final_array, loop through the dictionary, and add each anagram's list the the final array.
        4. Return the final array.
        '''
        if not strs:
            return [[]]
        if strs == [""]:
            return [[""]]

        anagram_to_val_dict = collections.defaultdict(list)

        for string in strs:
            this_str_sorted = str(sorted(string))
            anagram_to_val_dict[this_str_sorted].append(string)

        final_arr = []
        for key in anagram_to_val_dict.keys():
            final_arr.append(anagram_to_val_dict.get(key))
        return final_arr
