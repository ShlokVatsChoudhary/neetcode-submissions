class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if(m<n):
            return ""
        ans = Counter(t)
        check = {}
        mini = sys.maxsize
        left = 0
        start = -1
        
        for i in range(m):
            check[s[i]] = check.get(s[i],0) + 1

            is_subset = all(check.get(k, 0) >= v for k, v in ans.items())
            while(is_subset):
                if i - left + 1 < mini:
                    mini = i - left + 1
                    start = left
                check[s[left]] = check.get(s[left],0) - 1
                left += 1
                is_subset = all(check.get(k, 0) >= v for k, v in ans.items())
        
        return s[start:start + mini] if start != -1 else ""