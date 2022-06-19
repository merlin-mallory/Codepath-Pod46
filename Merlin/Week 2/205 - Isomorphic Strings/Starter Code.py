class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        Given two strings s and t, determine if they are isomorphic.

        Two strings s and t are isomorphic if the characters in s can be replaced to get t.

        All occurrences of a character must be replaced with another character while preserving the order of characters.
        No two characters may map to the same character, but a character may map to itself.

        Example 1:

        Input: s = "egg", t = "add"
        Output: true
        Example 2:

        Input: s = "foo", t = "bar"
        Output: false
        Example 3:

        Input: s = "paper", t = "title"
        Output: true

        Constraints:

        1 <= s.length <= 5 * 104
        t.length == s.length
        s and t consist of any valid ascii character.

        Plan 1:
        1. Create two new empty strings: s_new and t_new
        2. Create two sets: s_set and t_set. These will keep track of unique values in each string.
        2. Set s_counter and t_counter to 0.
        3. Loop through both strings.
            4. If the char is in the proper set, then add the appropriate counter to the appropriate new string.
            5. Else, add the char to the proper set, appropriate counter += 1, and add appropriate counter to the
            appropriate new string.
        6. Loop through both new strings, and if there is a mismatch, then return False. If we reach the end of both
        strings, then return True.
        7. Time: O(n)
        8. Space: O(n)

        Plan 2:
        1. Create two mapping_dicts. Keys: Unique char in s, Values: Corresponding char in t. Other is flipped
        2. Fill up the first dict. Loop through s and t.
            3. If s[i] not in mapping_dict, then add key s[i] with value t[i].
            4. Else, if mapping_dict[s[i]] != t[i], then return False
        5. Fill up the second dict (same actions)
        6. If we reach this point without returning False, then we know that the strings are isomorphic, so return True.
        7. Time: O(n), where n = len(s) + len(t)
        8. Space: O(1) (the max size of the dicts will be the allowable ASCII characters, which is constant)
        '''

        s_dict = {}
        t_dict = {}

        for c1, c2 in zip(s, t):
            if (c1 not in s_dict) and (c2 not in t_dict):
                s_dict[c1] = c2
                t_dict[c2] = c1
            elif s_dict.get(c1) != c2 or t_dict.get(c2) != c1:
                return False

        return True


