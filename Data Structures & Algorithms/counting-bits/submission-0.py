class Solution:
    def countBits(self, n: int) -> List[int]:
        Listt = []
        for x in range(0,n+1):
            c = 0
            while x:
                x &= x-1
                c += 1
            Listt.append(c)
            n = n-1
        return Listt