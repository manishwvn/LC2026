# Last updated: 8/20/2026, 1:57:01 AM
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        cnt = Counter(ranks)
        if len(set(suits)) == 1:
            return "Flush"
        elif max(cnt.values()) >= 3:
            return "Three of a Kind"
        elif max(cnt.values()) == 2:
            return "Pair"
        else:
            return "High Card"
        