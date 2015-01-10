class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x ==0:
            return 0
        if x == 1:
            return 1
        low = 1
        high = x-1
        while low<high:
            mid = low + (high-low)/2
            if x/mid>=mid and x/(mid+1)<mid+1:
                return mid
            elif x/mid>mid:
                low = mid+1
            elif x/mid<mid:
                high = mid-1
        return low