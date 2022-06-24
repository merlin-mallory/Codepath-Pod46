class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        https://leetcode.com/problems/isomorphic-strings/description/
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

        Plan #1:
        1. Create 2 dictionaries. from_s_to_t_dict will map characters from s to t. from_t_to_s_dict will map
        characters from t to s.
        2. Loop through the strings and create dictionaries.While we construct the dictionaries, we will check if the
        current character is currently in the dictionary.
            3. If the char is not in dictionary, then we will map it.
            4. Else if the current char mismatches the key's result, then return False.
            5. Else continue
        6. If we can construct both dictionaries without returning False, then we've got an isomorphic string,
        so return True.
        7. Time: Looping through the strings is O(m + n), where m is len(s) and n is len(t), which simplifies to O(
        n).
        8. Space: O(1) space. Because we are limited to using valid ascii characters, the maximum size of the
        dictionary is limited to a constant number, which is the number of valid ascii characters.
        '''

        from_s_to_t_dict = {}
        from_t_to_s_dict = {}

        # Constructing the dictionaries. The zip syntax loops through the two string simultaneously.
        for c1, c2 in zip(s,t):
            if (c1 not in from_s_to_t_dict) and (c2 not in from_t_to_s_dict):
                from_s_to_t_dict[c1] = c2
                from_t_to_s_dict[c2] = c1
            elif (from_s_to_t_dict.get(c1) != c2) or (from_t_to_s_dict.get(c2) != c1):
                return False

        return True

        # Attempt 1
        # from_s_to_t_dict = {}
        # from_t_to_s_dict = {}
        #
        # for i in range(len(s)-1):
        #     if s[i] not in from_s_to_t_dict:
        #         from_s_to_t_dict[s[i]] = t[i]
        #     elif s[i] != from_s_to_t_dict[s[i]]:
        #         return False
        #
        # for j in range(len(t)-1):
        #     if t[j] not in from_t_to_s_dict:
        #         from_t_to_s_dict[t[j]] = s[j]
        #     elif s[j] != from_s_to_t_dict[s[j]]:
        #         return False
        #
        # for k in range(len(s)-1):
        #     if from_s_to_t_dict[s[k]] != t[k]:
        #         return False
        #
        # for l in range(len(t)-1):
        #     if from_t_to_s_dict[t[l]] != s[k]:
        #         return False
        #
        # return True

