class Solution:
    
    def getTargetCopy(self, original, cloned, target):
        return self.getTarget(cloned, target.val)
    
    def getTarget(self, tree, value):
        # Base Case - Empty Tree
        if tree == None:
            return None
        # Base Case - Found Target
        if tree.val == value:
            return tree

        return self.getTarget(tree.left, value) or self.getTarget(tree.right, value)
