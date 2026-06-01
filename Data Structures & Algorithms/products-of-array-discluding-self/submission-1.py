class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_mul=1
        zero_mul=1
        zero_count=0
        for i in nums: 
            total_mul*=i
            if i == 0:
                zero_count += 1
            else:
                zero_mul *= i
        if zero_count > 1:
            zero_mul = 0
        output=[]
        for i in nums:
            if i==0:
                output.append(zero_mul)
                continue  
            output.append(total_mul//i)
        return output            