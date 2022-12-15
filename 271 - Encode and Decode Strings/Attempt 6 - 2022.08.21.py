class Codec:
    """
    Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and
    is decoded back to the original list of strings.

    Machine 1 (sender) has the function:

    string encode(vector<string> strs) {
      // ... your code
      return encoded_string;
    }
    Machine 2 (receiver) has the function:
    vector<string> decode(string s) {
      //... your code
      return strs;
    }
    So Machine 1 does:

    string encoded_string = encode(strs);
    and Machine 2 does:

    vector<string> strs2 = decode(encoded_string);
    strs2 in Machine 2 should be the same as strs in Machine 1.

    Implement the encode and decode methods.

    You are not allowed to solve the problem using any serialize methods (such as eval).

    Input: dummy_input = ["Hello","World"]
    Output: ["Hello","World"]
    Explanation:
    Machine 1:
    Codec encoder = new Codec();
    String msg = encoder.encode(strs);
    Machine 1 ---msg---> Machine 2

    Machine 2:
    Codec decoder = new Codec();
    String[] strs = decoder.decode(msg);
    Example 2:

    Input: dummy_input = [""]
    Output: [""]
    """
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        Plan:
        1. Loop through strs. Construct a substring that contains len(my_str) + # + my_str. Append that to the final
        array.
        2. Join and return the final array.
        """
        encoded_str = []
        for my_str in strs:
            my_str_len = len(my_str)
            encoded_str.append(str(my_str_len) + "#" + my_str)
        return "".join(encoded_str)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        Plan:
        1. Initialize i to 0, and loop until i > len(s)-1. Initialize decoded_arr to an array.
        2. Grab the length of the first substring by iterating left until we hit the #. Then convert that length to
        an int.
        3. Iterate i to the next index, and slice s from i to i+length. Append the slice to the decoded_arr.
        4. Return the decoded_arr
        """
        i = 0
        decoded_arr = []
        while i < len(s)-1:
            length_substring = []
            while s[i].isnumeric():
                length_substring.append(s[i])
                i += 1
            length_int = int("".join(length_substring))
            i += 1
            decoded_arr.append(s[i:i+length_int])
            i += length_int
        return decoded_arr


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
