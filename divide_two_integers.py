class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor ==0:
            return MAX_INT
        elif dividend == 0:
            return 0
        sign = 1
        if  dividend>0 and divisor<0 :
            sign = 0
            divisor = -divisor
        elif dividend<0 and divisor > 0:
            sign = 0
            dividend = -dividend
        elif dividend<0 and divisor<0:
            divisor = -divisor
            dividend = -dividend
            
            
        
        y = dividend
        x = divisor
        quo = 0
        while y>= x:
            quo1 = 1
            x1 = x
            while y-x1>=x1:
                x1 = x1+x1
                quo1 = quo1+quo1
            quo +=quo1
            y = y-x1
        if sign:
            return quo
        else:
            return -quo