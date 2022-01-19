class Solution:
    def toHex(self, num: int) -> str:
        num2hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        answer = ''
        
        if num==0: return "0"
        
        #(-2)**31 <= num <= 2**31-1 
        #for negative num, two's complement = 2**32-num
        
        elif num<0:
            num += 2**32
            
        while 0<num:
            answer += num2hex[num%16]
            num //= 16
            
        return answer[::-1]
        