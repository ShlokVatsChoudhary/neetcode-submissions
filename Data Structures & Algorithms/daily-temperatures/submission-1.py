class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]: 
                stack_top_index = stack.pop()
                result[stack_top_index] = i - stack_top_index
            stack.append(i)
        return result 