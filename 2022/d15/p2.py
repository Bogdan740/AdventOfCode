f = open("sample.txt", "r")

sensBeac = [ [(int(k[2][2:-1]),int(k[3][2:-1])), (int(k[-2][2:-1]),int(k[-1][2:]))] for k in [(line.split()) for line in f.read().split("\n")]]
sensBeac = sorted([ ((sx,sy),(bx,by),abs(sx - bx) + abs(sy-by)) for (sx,sy),(bx,by) in sensBeac], key=lambda x:x[0] )

mx = 20
for y in range(1,mx+1):
  x = 0
  for (sx,sy),(bx,by),distSB in sensBeac:
    distSR = abs(sy - y)
    diff = distSB - distSR
    if(distSB >= distSR):
      l,r = (sx-diff,sx+diff+1 if sx+diff+1 < mx else mx)
      if(l <= x and r > x):
        x = r
  if(x!=mx):
    print(x,y, x *4000000 + y)
    break