def transformString(s: str) -> str:
    index_mapping = {}
    new_str = []

    for i, c in enumerate(s):
        if c not in index_mapping:
            index_mapping[c] = i
        new_str.append(str(index_mapping[c]))

    return " ".join(new_str)


def isIsomorphic(s: str, t: str) -> bool:
    return transformString(s) == transformString(t)

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