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
        1. Create encoded_str as an array.
        2. Loop through strs. Calculate the length of each string. Append str(length) + "#" + my_str to encoded_str.
        3. Join and return encoded_str
        4. Time: O(n). Space: O(n)
        """
        encoded_str = []
        for my_str in strs:
            length = str(len(my_str))
            encoded_str.append(length + "#" + my_str)
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        Plan:
        1. Initialize i to 0, and decoded_str as an array.
        2. While i < len(s),
            3. Create substring_arr.
            4. While s[i] != "#":
                5. substring_arr.append(s[i])
            6. length_as_str = "".join(substring_arr)
            7. length_as_int = int(length_as_str)
            8. i += 1
            9. Slice from (i : i+length), and append that slice to decoded_str.
            10. i += length
        11. Return decoded_str
        """
        i, decoded_str = 0, []
        while i < len(s):
            substring_arr = []
            while s[i] != "#":
                substring_arr.append(s[i])
                i += 1
            length_as_str = "".join(substring_arr)
            length_as_int = int(length_as_str)
            i += 1
            this_slice = s[i:i+length_as_int]
            decoded_str.append(this_slice)
            i += length_as_int
        return decoded_str

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
