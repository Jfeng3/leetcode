class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        start = 0
        end = len(num)-1
        while start<end:
            if target > num[start]+num[end]:
                start +=1
            elif target<num[start]+num[end]:
                end -=1
            else:
                return (start+1,end+1)