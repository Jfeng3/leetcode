class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        
        low = 0
        high = len(A)-1
        while(low<=high):
            mid = low+(high-low)/2
            if target == A[mid]:
                return mid
            elif target>A[mid]:
                low = mid+1
            else:
                high = mid-1
        return low