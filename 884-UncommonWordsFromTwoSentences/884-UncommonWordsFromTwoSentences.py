# Last updated: 10/7/2026, 3:03:58 PM
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        counts = defaultdict(int)

        for word in s1.split():
            counts[word] += 1

        for word in s2.split():
            counts[word] += 1
        
        result = []
        for word, count in counts.items():
            if count == 1:
                result.append(word)

        return result
        