class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        return self.findMin_re(num,0,len(num)-1)
        
    def findMin_re(self,num,start,end):
        if start == end:
            return num[start]
        if start+1 == end:
            if num[start]<=num[end]:
                return num[start]
            else:
                return num[end]
        mid = start + (end-start)/2
        if num[end]>num[mid]:
            return self.findMin_re(num,start,mid)
        elif num[end]<num[mid]:
            return self.findMin_re(num,mid+1,end)
        elif num[start]>num[mid]:
            return self.findMin_re(num,start+1,mid)
        elif num[start]<num[mid]:
            return self.findMin_re(num,start,mid-1)
        else:
            return min(self.findMin_re(num,start,mid),self.findMin_re(num,mid+1,end))
        