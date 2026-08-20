# Last updated: 8/20/2026, 2:08:01 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        if not root or not target: return []
        
        elif k == 0: return [target.val]
        
        #make graph
        graph = defaultdict(list)
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
                
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)
                
        #bfs on graph
        result = []
        queue = deque()
        depth = 0
        visited = set()
        queue.append(target)
        
        while queue and depth <= k:
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node not in visited:
                    for neigh in graph[node]:
                        queue.append(neigh)
                    
                    if depth == k:
                        result.append(node.val)
                visited.add(node)   
            depth += 1
        
        return result
        
        