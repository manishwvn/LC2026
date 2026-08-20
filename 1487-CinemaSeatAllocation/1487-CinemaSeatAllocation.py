# Last updated: 8/20/2026, 2:03:03 AM
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        hm = {}

        for reserve in reservedSeats:
            row, seat = reserve
            if row not in hm:
                hm[row] = set([])
            hm[row].add(seat)

        free_rows = n - len(hm.keys())
        groups_free_rows = free_rows * 2

        groups_problematic = 0

        for row, seats in hm.items():

            block_a = True
            for seat in [2, 3, 4, 5]:
                if seat in seats:
                    block_a = False
                    break

            block_b = True
            for seat in [4, 5, 6, 7]:
                if seat in seats:
                    block_b = False
                    break

            block_c = True
            for seat in [6, 7, 8, 9]:
                if seat in seats:
                    block_c = False
                    break

            if block_a and block_c:
                groups_problematic += 2

            elif block_a:
                groups_problematic += 1

            elif block_c:
                groups_problematic += 1
            
            elif block_b:
                groups_problematic += 1

        return groups_free_rows + groups_problematic