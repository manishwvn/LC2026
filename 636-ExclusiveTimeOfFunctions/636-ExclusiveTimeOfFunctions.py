# Last updated: 8/20/2026, 2:10:22 AM
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        res = [0] * n
        stack = []

        for log in logs:
            func_id, status, time = log.split(':')
            func_id, time = int(func_id), int(time)

            if status == "start":
                stack.append((func_id, time))

            else:
                func_id, start_time = stack.pop()
                duration = time - start_time + 1
                res[func_id] += duration

                if stack:
                    res[stack[-1][0]] -= duration

        return res