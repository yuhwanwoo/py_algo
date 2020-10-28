n=int(input())

dummy=[[0]*(n+1) for _ in range(n+1)]

k=int(input())
for _ in range(k):
    a,b=map(int,input().split())
    dummy[a][b]=1

l=int(input())
info=[]
for _ in range(l):
    a,b=input().split()
    info.append((int(a),b))


time=0

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def rot_direction(direction,c):
    if c=="L":
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4
    return direction

time=0
index=0
x,y=1,1
direction=0
q=[(x,y)]
while True:
    nx=x+dx[direction]
    ny=y+dy[direction]
    
    if nx>=1 and nx<=n and ny>=1 and ny<=n and dummy[nx][ny]!=2:
        if dummy[nx][ny]==0:
            dummy[nx][ny]=2
            q.append((nx,ny))
            px,py=q.pop(0)
            dummy[px][py]=0
        if dummy[nx][ny]==1:
            dummy[nx][ny]=2
            q.append((nx,ny))
    else:
        time+=1
        break
    x,y=nx,ny
    time+=1
    if index<l and time==info[index][0]:
        direction=rot_direction(direction,info[index][1])
        index+=1
    
print(time)
    
