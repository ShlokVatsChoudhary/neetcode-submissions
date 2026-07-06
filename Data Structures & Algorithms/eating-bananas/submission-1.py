class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles) 
        if h == len(piles): return n
        piles.sort()
        left,right = 1,n
        best = right

        while(left<=right):
            mid = left + (right-left) // 2
            th = sum(math.ceil(pile / mid) for pile in piles)
            if(th <= h):
                best = min(best,mid)
                right = mid - 1
            else:
                left = mid + 1
        return best