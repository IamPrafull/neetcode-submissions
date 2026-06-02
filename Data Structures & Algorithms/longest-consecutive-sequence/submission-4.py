class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        arr=sorted(set(nums))
        count=1
        max_count=1
        for i in range(0,len(arr)-1):
            if ((arr[i]+1)==arr[i+1]):
                count+=1
            else:
                max_count=max(max_count,count)
                count=1
        return max(max_count,count)
        