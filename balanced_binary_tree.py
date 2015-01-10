# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
            print "range1,range2",range1,range2
            if range1[0]>range2[0]+1 or range2[0]>range1[0]+1:
                return False
            range[0]= max(range1[0],range2[0])+1
            print range
            return True
            



sol = Solution()
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(2)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(3)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(3)
root.right.left.left = TreeNode(3)
root.right.left.right = TreeNode(3)
root.left.left.left.left = TreeNode(4)
root.left.left.left.right = TreeNode(4)

height = [0]
assert sol.isBalanced_re(root,height)
print height