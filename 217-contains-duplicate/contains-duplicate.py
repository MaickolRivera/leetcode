class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        for count in count.values():
            if count >= 2:
                return True
        return False