class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A) == 0:
            return -1
        if len(A) == 1:
            return 0 if target == A[0] else -1
        return self.search_re(A,0,len(A)-1,target)
        
    def search_re(self,A,m,n,target):
        if m==n and target ==A[m]:
            return m
        elif (m ==n and target!=A[m]) or m>n:
            return -1
            
        mid = m + (n-m)/2
        if A[mid] == target:
            return mid
        elif A[m]<=A[mid] and target>=A[m] and target<A[mid]:
            return self.search_re(A,m,mid-1,target)
        elif A[m]>A[mid] and (target>=A[m] or target<A[mid]):
            return self.search_re(A,m,mid-1,target)
        elif A[m]>A[mid] and (target<A[m] and target>A[mid]):
            return self.search_re(A,mid+1,n,target)
        elif A[m]<=A[mid] and (target<A[m] or target>A[mid]):
            return self.search_re(A,mid+1,n,target)