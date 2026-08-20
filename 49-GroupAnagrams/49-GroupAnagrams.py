# Last updated: 8/20/2026, 2:19:24 AM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}

        for str in strs:
            counts = [0] * 26

            for char in str:
                counts[ord(char) - ord('a')] += 1

            if tuple(counts) in result:
                result[tuple(counts)].append(str)
            else:
                result[tuple(counts)] = [str]

        return list(result.values())