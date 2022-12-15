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
        '''
        import collections
        mapping_dict_s = collections.defaultdict(int)   # Keys: Letters, Values: Frequency count
        mapping_dict_t = collections.defaultdict(int)

        for char in s:
            mapping_dict_s[char] += 1

        for char in t:
            mapping_dict_t[char] += 1

        for char in s:
            if mapping_dict_s.get(char) != mapping_dict_t.get(char):
                return False

        for char in t:
            if mapping_dict_s.get(char) != mapping_dict_t.get(char):
                return False

        return True
