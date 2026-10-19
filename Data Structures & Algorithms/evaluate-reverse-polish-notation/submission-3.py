class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        runningSum = 0
        stack = []
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                x = int(stack.pop())
                y = int(stack.pop())
                match i:
                    case "+":
                        stack.append(y + x)
                    case "-":
                        stack.append(y - x)
                    case "*":
                        stack.append(y * x)
                    case "/":
                        stack.append(int(y / x))
        return stack[-1]

        