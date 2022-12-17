f = open("input.txt", "r")

inp = f.read()
# We can treat this like a directed graph where we can only travel towards a square
# that is one lower or one higher than our current position
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
graph[end[0]][end[1]] = ord("z")# Set the end value as the highest possible value
graph[start[0]][start[1]] = ord("a")# Set the end value as the highest possible value

# Basically depth first search
def distanceToHighestPoint(graph,start,end):
  # Define a 2D array to check if we have been aa vertex before or not
  visited = [ [False for _ in i] for i in graph]
  depth = 0
  queue = [start]
  nbours = [(1,0), (-1,0), (0,1), (0,-1)]
  while(len(queue) != 0):
    for _ in range(len(queue)):
      # Current location
      x,y = queue.pop(0)
      # Check if we have reached the end node
      if(x == end[0] and y == end[1]):
        return depth
      # Add all valid nbours to 
      for i,j in nbours:
        nx,ny = x + i, y + j
        if(0<= nx < len(graph) and 0<= ny < len(graph[0]) and (not visited[nx][ny])):
          currentHeight = graph[x][y]
          nHeight = graph[nx][ny]
          if(nHeight - currentHeight <= 1):
            visited[nx][ny] = True
            queue.append((nx,ny))
      
    # Increment the depth
    depth+=1
  return depth
  
  
print(distanceToHighestPoint(graph,start,end))
  
  
      