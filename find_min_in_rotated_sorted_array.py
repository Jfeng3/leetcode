class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):

        return self.findMin_re(num,0,len(num)-1)
        
    def findMin_re(self,num,start,end):
        if start == end:
            return num[start]
        if start+1 == end:
            return min(num[start],num[end])
        mid = start + (end-start)/2
        if num[mid]<num[start]:
            return self.findMin_re(num,start+1,mid)
        elif num[mid]>num[end]:
            return self.findMin_re(num,mid+1,end)
        else:
            return num[start]