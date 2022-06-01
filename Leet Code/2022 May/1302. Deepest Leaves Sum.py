class Solution:
    def deepestLeavesSum(self, root):
        queue = [root]
        result = 0
        while len(queue) > 0:
            size = len(queue)
            level_nodes = []
            while size > 0:
                node = queue.pop(0)
                size = size - 1
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result = sum(level_nodes)
        return result