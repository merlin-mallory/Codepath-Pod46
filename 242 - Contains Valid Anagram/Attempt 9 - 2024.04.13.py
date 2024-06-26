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
        Hashset
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        import collections
        s_hashmap = collections.Counter(s)
        t_hashmap = collections.Counter(t)
        return s_hashmap == t_hashmap


