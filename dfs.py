from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	def addEdge(self, u, v):
		self.graph[u].append(v)
	def DFSUtil(self, v, visited,key):
		visited.add(v)
		print(v, end=' ')
		if(v==key):
			return
		for neighbour in self.graph[v]:
			if(v==key):
				break
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited,key)
	def DFS(self, v,key):
		visited = set()
		self.DFSUtil(v, visited,key)
	
if __name__ == "__main__":
	g = Graph()
	g.addEdge(4, 5)
	g.addEdge(5, 3)
	g.addEdge(4, 3)
	g.addEdge(2, 5)
	g.addEdge(2, 4)
	g.addEdge(3, 2)
	g.addEdge(3,8)
	g.addEdge(3,7)
	g.addEdge(8,7)
	g.addEdge(2,7)
	g.addEdge(2,8)
	print("Following is DFS from (starting from vertex 2)")
	g.DFS(4,5)
'''Following is DFS from (starting from vertex 2)
4 5 3 2 7 8 '''
