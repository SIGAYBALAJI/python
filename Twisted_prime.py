class Solution:
    def is_Prime(self,n):
        for i in range(2,int((n**0.5))+1):
            if n%i==0:
                return False
        return True
    def is_twited(self,n):
        res1=self.is_Prime(n)
        reversed_n=int(str(n)[::-1])
        res2=self.is_Prime(reversed_n)
        return int(res1 and res2)
   
