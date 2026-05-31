class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res=[]
        while(k!=0):
            # for top frequency key
            key=max(d,key=d.get)
            res.append(key)
            d[key]=0
            k-=1
        return res


