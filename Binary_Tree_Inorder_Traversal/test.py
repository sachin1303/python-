from solution import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node3 = TreeNode(3)
node2 = TreeNode(2,node3)
node1 = TreeNode(1,None,node2)
assert [1,3,2] == Solution().inorderTraversal(node1) , 'Test Case Failed'
print ("successfully done")