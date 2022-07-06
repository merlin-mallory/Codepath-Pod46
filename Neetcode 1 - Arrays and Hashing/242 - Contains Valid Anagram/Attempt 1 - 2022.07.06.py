class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        https://leetcode.com/problems/valid-anagram/

        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
        using all the original letters exactly once.

        Input: s = "anagram", t = "nagaram"
        Output: true

        Input: s = "rat", t = "car"
        Output: false

        Constraints:
        1 <= s.length, t.length <= 5 * 10^4
        s and t consist of lowercase English letters.

        Plan:
        1. Create s_dict and t_dict (keys: letters, values: count)
        2. Loop through both strings and create both dictionaries.
        3. Loop through s_dict and check if there's a mismatch in t_dict. If a mismatch is found, then return False.
        Otherwise return true.
        '''
        from collections import defaultdict

        s_dict = collections.defaultdict(int)
        t_dict = collections.defaultdict(int)

        for char in s:
            s_dict[char] += 1

        for char in t:
            t_dict[char] += 1

        for key in s_dict:
            if s_dict[key] != t_dict[key]:
                return False

        for key in t_dict:
            if t_dict[key] != s_dict[key]:
                return False

        return True

