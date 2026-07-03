class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n,m = len(s1),len(s2)
        if n > m:
            return False

        arr1 = Counter(s1)
        arr2 = Counter(s2[0:n])

        if arr1 == arr2 :
            return True

        for r in range(n,len(s2)):
            temp = s2[r]
            temp2 = s2[r-n]
            arr2[temp] = arr2.get(temp, 0) + 1
            arr2[temp2] = arr2.get(temp2, 0) - 1

            if arr1 == arr2:
                return True
        return False