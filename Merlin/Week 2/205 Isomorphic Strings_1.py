def isIsomorphic(s: str, t: str) -> bool:
    '''
    Definition:
    If we can swap all of the characters in s with different characters to form t,
    then strings s and t are isomorphic.

    Input: s = "egg", t = "add"
    Output: True

    Input: s = "foo", t = "bar"
    Output: False

    Input s = "paper", t = "title"
    Output: True

    Restrictions:
    1. len(s) = len(t)
    2. s and t can be any Unicode character
    3. len(s) >= 1
    4. len(s) <= 5* 10^4

    Plan:
    1. Loop through every char in t, and mutate all of the corresponding characters in s.
    2. Check if v === t. If true, return true. Otherwise, return false.
    '''

    array_s = list(s)
    array_t = list(t)
    print(array_s, array_t)

    for i in range(len(t)):
        current_char_t = array_t[i]
        corresponding_char_s = array_s[i]

        for j in range(len(s)):
            if array_s[j] == corresponding_char_s:
                array_s[j] = current_char_t

    print("Final arrays:", array_s, array_t)

    if array_s == array_t:
        return True
    else:
        return False

    # for i in range(len(t)):
    #
    #     current_char_t = t[i]
    #     corresponding_char_s = s[i]
    #     temp_str = copy.deepcopy(s)
    #     for j in range(len(s)):
    #         if temp_str[j] == corresponding_char_s:
    #             temp_str[j] = current_char_t
    #
    # if temp_str == t:
    #     return True
    # else:
    #     return False


s = "egg"
t = "add"
result = isIsomorphic(s, t)
print(result)

s = "foo"
t = "bar"
result = isIsomorphic(s, t)
print(result)

s = "paper"
t = "title"
result = isIsomorphic(s, t)
print(result)