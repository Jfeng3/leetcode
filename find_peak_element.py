class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) == 0 or len(num) == 1:
            return 0
        
        low = 0
        high = len(num)-1
        while low<high:
            mid = low + (high-low)/2
            t1 = self.getDeri(num,mid)
            t2 = self.getDeri(num,mid+1)
            if t1 and not t2:
                return mid+1
            elif t1:
                low = mid+1
            elif not t1:
                high = mid
        return low
        
    def getDeri(self,num,i):
        if i<len(num)-1:
            return num[i+1]-num[i]>0
        elif i == len(num)-1:
            return False