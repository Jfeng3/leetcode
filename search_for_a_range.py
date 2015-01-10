class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        x1 = self.searchFirst(A,target)
        x2 = self.searchLast(A,target)
        return[x1,x2]
        
    def searchFirst(self,A,target):
        low = 0
        high = len(A)-1
        while low<=high:
            mid = low + (high-low)/2
            if A[mid] == target and mid == 0:
                return 0
            elif A[mid] == target and A[mid-1]!=target:
                return mid
            elif A[mid]>=target:
                high = mid-1
            elif A[mid]<target:
                low = mid+1
        if high<low:
            return -1
    def searchLast(self,A,target):
        low = 0
        high = len(A)-1
        while low<=high:
            mid = low + (high-low)/2
            if A[mid] == target and mid == len(A)-1:
                return len(A)-1
            elif A[mid] == target and A[mid+1]!=target:
                return mid
            elif A[mid] == target and A[mid+1] ==target:
                low = mid+1
            elif A[mid]>target:
                high = mid-1
            elif A[mid]<target:
                low = mid+1
        if high<low:
            return -1