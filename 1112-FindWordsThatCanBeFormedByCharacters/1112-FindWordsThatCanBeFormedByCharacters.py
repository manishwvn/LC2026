# Last updated: 8/20/2026, 2:06:23 AM
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        
        sum_, chars_counter = 0, collections.Counter(chars)
        for word in words:
            word_counter = collections.Counter(word)
            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                sum_ += len(word)
        return sum_
        