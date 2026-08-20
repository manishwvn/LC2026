# Last updated: 8/20/2026, 1:57:39 AM
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)

        size = 4 * n
        seg_len    = [0] * size
        seg_lchar  = [''] * size
        seg_rchar  = [''] * size
        seg_prefix = [0] * size
        seg_suffix = [0] * size
        seg_best   = [0] * size

        def pull(node, left, right):
            seg_len[node] = seg_len[left] + seg_len[right]
            seg_lchar[node] = seg_lchar[left]
            seg_rchar[node] = seg_rchar[right]

            if seg_prefix[left] == seg_len[left] and seg_lchar[left] == seg_lchar[right]:
                seg_prefix[node] = seg_len[left] + seg_prefix[right]
            else:
                seg_prefix[node] = seg_prefix[left]

            if seg_suffix[right] == seg_len[right] and seg_rchar[right] == seg_rchar[left]:
                seg_suffix[node] = seg_len[right] + seg_suffix[left]
            else:
                seg_suffix[node] = seg_suffix[right]

            best = seg_best[left] if seg_best[left] > seg_best[right] else seg_best[right]
            if seg_rchar[left] == seg_lchar[right]:
                cross = seg_suffix[left] + seg_prefix[right]
                if cross > best:
                    best = cross
            seg_best[node] = best

        def build(node, l, r):
            if l == r:
                c = s[l]
                seg_len[node] = 1
                seg_lchar[node] = c
                seg_rchar[node] = c
                seg_prefix[node] = 1
                seg_suffix[node] = 1
                seg_best[node] = 1
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            pull(node, 2 * node, 2 * node + 1)

        def update(node, l, r, idx, ch):
            if l == r:
                seg_lchar[node] = ch
                seg_rchar[node] = ch
                # length/prefix/suffix/best remain 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)
            pull(node, 2 * node, 2 * node + 1)

        build(1, 0, n - 1)

        result = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            result.append(seg_best[1])

        return result