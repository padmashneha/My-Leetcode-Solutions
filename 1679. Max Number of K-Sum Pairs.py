def maxOperations(self, nums: List[int], k: int) -> int:
        i,j,cnt = 0,len(nums)-1,0
        nums = sorted(nums)
        while i<j:
            total = nums[i]+nums[j]
            if total<=k: i+=1
            if total>=k: j-=1
            if total==k: cnt+=1
        return cnt
