class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.sumofsquares(n)
            if n==1:
                return True
        return False
        
    def sumofsquares(self,n):
        output=0
        while n>0:
            last_digit=n%10
            output+=last_digit**2
            n=n//10
        return output
        

        
        