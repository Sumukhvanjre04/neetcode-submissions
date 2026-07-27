class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        my_list=[(values,keys) for keys, values in freq.items()]
        my_list.sort()
        res=[]
        while len(res)<k:
            res.append(my_list.pop()[1])
        return res
        
        

            


        
       

        