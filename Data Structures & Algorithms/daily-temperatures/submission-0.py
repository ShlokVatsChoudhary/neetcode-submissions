class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        st = [] 
        c = len(t)
        final = [0] * c
        for i in range(c):
            while st and t[i] > t[st[-1]]:
                prev_index = st.pop()
                final[prev_index] = i - prev_index
            st.append(i)
        return final