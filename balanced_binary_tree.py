# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        range = [-1]
        return self.isBalanced_re(root,range)
        
    def isBalanced_re(self,root,range):
        if not root:
            range[0]= 0
            return True
        else:
            range1 = [-1]
            range2 = [-1]
            if not self.isBalanced_re(root.left,range1):
                return False
            elif not self.isBalanced_re(root.right,range2):
                return False
            
            elif range1[0]>range2[0]+1 or range2[0]>range1[0]+1:
                return False
            range[0]= max(range1[0],range2[0])+1
            return True