import math
v=int(input("Enter the number of vertices :"))
points=[]
for i in range(0,v):
  x,y=map(float,input(f"Enter the coordinate for vertex {i+1} : ").split())
  points.append([x,y])
print(points) 
x1=pow(points[0][0]-points[v-1][0],2)
y1=pow(points[0][1]-points[v-1][1],2)

sq1=math.sqrt(x1+y1)

for i in range(0,v-1):
  x2=pow(points[i][0]-points[i+1][0],2)
  y2=pow(points[i][1]-points[i+1][1],2)
  sq2=math.sqrt(x2+y2)
  print(f"edge {i+1} : "+str(sq2))
  
print(f"Edge {v-1} : "+str(sq1))  

