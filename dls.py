v=14
graph=[[] for i in range(v)]
visited=[False for i in range(v)]
def DFS(s,dest,cur_depth,depth,visited):
  if s==dest:
    print(s, '-destination',end=' ')
    return
  visited[s]=True
  print(s,end=' ')
  for p in graph[s]:
    if visited[p]==False and cur_depth<depth:
      DFS(p,dest,cur_depth+1,depth,visited)

def addedge(a,b):
  graph[a].append(b)
  graph[b].append(a)

addedge(0, 1)
addedge(0, 2)
addedge(0, 3)
addedge(1, 4)
addedge(1, 5)
addedge(2, 6)
addedge(2, 7)
addedge(3, 8)
addedge(8, 9)
addedge(8, 10)
addedge(9, 11)
addedge(9, 12)
addedge(9, 13)
source=int(input("Enter source : "))
destination=int(input("Enter destination : "))
depth=int(input('Enter depth Limit: '))
DFS(source,destination,0,depth,visited)
'''Enter source : 0
Enter destination : 3
Enter depth Limit: 5
0 1 4 5 2 6 7 3 -destination''' 
