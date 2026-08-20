# Last updated: 8/20/2026, 2:09:51 AM
class Solution:
    def calPoints(self, operations: List[str]) -> int:

        result = []

        for op in operations:
           
            if op == "C" and result:
                result.pop()
            
            elif op == "D" and result:
                result.append(result[-1] * 2)

            elif op == "+" and len(result) >= 2:
                result.append(result[-1] + result[-2])
            
            else:
                result.append(int(op))
        print(result)
        return sum(result)


        