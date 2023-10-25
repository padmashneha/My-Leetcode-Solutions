def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
   
        if len(set(d.values())) == len(set(arr)):
            return True
        else:
            return False
