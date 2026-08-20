# Last updated: 8/20/2026, 2:16:51 AM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                num2, num1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
        return stack[0]
                    