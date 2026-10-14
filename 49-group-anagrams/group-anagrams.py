from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        result = []

        for i in strs:
            newgroups = tuple(sorted(i))
            groups[newgroups].append(i)

        for i in groups:
            result.append(groups[i])

        return result