class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        final = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                old_i, old_temp = stack.pop()
                final[old_i] = i - old_i

            stack.append((i, temp))

        return final
        