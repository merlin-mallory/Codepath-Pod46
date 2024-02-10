class TimeMap:
    '''
    981 - Time Based Key-Value Store

    https://leetcode.com/problems/time-based-key-value-store/

    Design a time-based key-value data structure that can store multiple values for the same key at different time
    stamps and retrieve the key's value at a certain timestamp.

    Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time
    timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with
    timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the
    largest timestamp_prev. If there are no values, it returns "".

    Example 1:
    Input:
    ["TimeMap", "set", "get", "get", "set", "get", "get"]
    [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    Output:
    [null, null, "bar", "bar", null, "bar2", "bar2"]
    Explanation:
    TimeMap timeMap = new TimeMap();
    timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
    timeMap.get("foo", 1);         // return "bar"
    timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and
                                   // timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
    timeMap.get("foo", 4);         // return "bar2"
    timeMap.get("foo", 5);         // return "bar2"

    Constraints:
    1 <= key.length, value.length <= 100
    key and value consist of lowercase English letters and digits.
    1 <= timestamp <= 10^7
    All the timestamps timestamp of set are strictly increasing.
    At most 2 * 10^5 calls will be made to set and get.

    Plan:
    Create defaultdict(list. Keys: Keys processed so far in the timemap. Values: List of [str_val, timestamp].
    Set: Simple addition to dict.
    Get: Extract the list of values for the particular key. Do binary search on this list, search for
    input_timestamp ==  dict_timestamp. If a match is found, return it. Otherwise, if the dict_timestamp <
    input_timestamp, update the cur_str.
    '''

    def __init__(self):
        '''
        '''
        import collections
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp, value])
        return None

    def get(self, key: str, timestamp: int) -> str:
        cur_vals = self.dict[key]
        l, r = 0, len(cur_vals)-1
        final_str = ""
        while l <= r:
            m = (l + r) // 2
            cur_timestamp = cur_vals[m]
            if cur_timestamp[0] == timestamp:
                return cur_vals[m][1]
            elif cur_timestamp[0] < timestamp:
                final_str = cur_vals[m][1]
                l = m + 1
            else:
                r = m - 1
        return final_str


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))            # "bar"
print(timeMap.get("foo", 3))            # "bar"
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))            # "bar2"
print(timeMap.get("foo", 5))            # "bar2"