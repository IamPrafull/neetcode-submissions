class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        i=0
        for num in nums:
            need=target-num
            if need in d:
                return [d[need],i]
            d[num]=i
            i+=1