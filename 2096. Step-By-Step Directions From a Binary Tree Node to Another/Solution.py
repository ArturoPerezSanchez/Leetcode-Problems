# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
		# make a graph
        self.connect(None, root, "")
		# BFS Traversal 
        visited = {startValue}
        queue = collections.deque([(startValue, "")])
        while queue:
            node, curr = queue.popleft()
            if node == destValue:
                return curr
            for nxt, direction in self.graph[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, curr + direction))
                    
    def connect(self, parent, child, direction):
		# shoud the moving direction inserting the node in the graph
        if parent and child:
            self.graph[parent.val].append((child.val, direction))
            self.graph[child.val].append((parent.val, "U"))
        if child.left:
            self.connect(child, child.left, "L")
        if child.right:
            self.connect(child, child.right, "R")

        

        
            
        

