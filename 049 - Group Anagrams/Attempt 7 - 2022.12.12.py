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
        1. Create a strs_dict. Keys: sorted anagram, Values: list containing all the strings with that anagram.
        2. Loop through strs. Calculate sorted_val = sorted(strs[i]). Append strs[i] to strs_dict[sorted_val].
        3. Return strs_dict.values().
        4. Time: O(N) for making strs_dict, O(n log k) for sorting each string, O(n) for the final return. Overall
        time complexity is O(n).
        5. Space: O(n).
        '''
        from collections import defaultdict
        strs_dict = defaultdict(list)  # Keys: sorted anagrams, Values: List containing all the strings grouped under
        # the anagram
        for i in range(len(strs)):
            sorted_val = str(sorted(strs[i]))
            strs_dict[sorted_val].append(strs[i])
        return strs_dict.values()

    # Optimal solution using ord instead of sorting:
    # ans = collections.defaultdict(list)
    #
    # for s in strs:
    #     count = [0] * 26
    #     for c in s:
    #         count[ord(c) - ord("a")] += 1
    #     ans[tuple(count)].append(s)
    # return ans.values()

