# Last updated: 10/7/2026, 3:02:43 PM
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        num.reverse()
        i = 0

        while k:
            d = k % 10
            if i < len(num):
                num[i] += d
            else:
                num.append(d)
            
            carry = num[i] // 10
            num[i] = num[i] % 10

            k //= 10
            k += carry
            i += 1
        
        num.reverse()
        return num


        