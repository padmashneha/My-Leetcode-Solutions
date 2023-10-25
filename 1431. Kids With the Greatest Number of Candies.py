def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        key = max(candies)
        return [i+extraCandies >= key for i in candies]
