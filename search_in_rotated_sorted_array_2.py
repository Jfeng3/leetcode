class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        return self.search_re(A,target,0,len(A)-1)
        
    def search_re(self,A,target,low,high):
        if low>high:
            return False
        mid = low + (high-low)/2
        if target == A[mid]:
            return True
        if A[mid]>A[low] or A[mid]>A[high]:
            if target >=A[low] and target<A[mid]:
                return self.search_re(A,target,low,mid-1)
            else:
                return self.search_re(A,target,mid+1,high)
        elif A[mid]<A[low] or A[mid]<A[high]:
            if target<=A[high] and target>A[mid]:
                return self.search_re(A,target,mid+1,high)
            else:
                return self.search_re(A,target,low,mid-1)

        else:
            return self.search_re(A,target,mid+1,high) or self.search_re(A,target,low,mid-1)