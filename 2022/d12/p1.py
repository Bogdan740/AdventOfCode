f = open("input.txt", "r")

inp = f.read()
# We can treat this like a directed graph where we can only travel towards a square
# that is at most one higher than our current square
graph = [ [ord(j) for j in i] for i in inp.split("\n")]
startIndicator = ord("S")
endIndicator = ord("E")

start = None
end = None

for i in range(len(graph)):
  for j,val in enumerate(graph[i]):
    if(val == startIndicator):
      start = (i,j)
    elif(val== endIndicator):
      end = (i,j)
graph[start[0]][start[1]] = ord("a") - 1

# Basically breadth first search
def distanceToHighestPoint(graph,start,end):
  # Define a 2D array to check if we have been a vertex before or not
  visited = [ [False for _ in i] for i in graph]
  depth = 0
  queue = [start]
  nbours = [(1,0), (-1,0), (0,1), (0,-1)]
  while(len(queue) != 0):
    for _ in range(len(queue)):
      x,y = queue.pop(0)
      if(x == end[0] and y == end[1]):
        return depth
      for i,j in nbours:
        nx,ny = x + i, y + j
        if(0<= nx < len(graph) and 0<= ny < len(graph[0]) and (not visited[nx][ny])):
          currentHeight = graph[x][y]
          nHeight = graph[nx][ny]
          # You can't climb but u can jump like 25 units and live lol, ok :p 
          if(nHeight - currentHeight <= 1):
            visited[nx][ny] = True
            queue.append((nx,ny))
      
    depth+=1
  return depth
  
print(distanceToHighestPoint(graph,start,end))
  
  
      