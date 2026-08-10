class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        digits="".join(map(str,digits))
        new_digits=int(digits)
        new_digits+=1
        digits=list(map(int,str(new_digits)))
        return digits
        