v=int(input("Enter the number of vertices:"))
points=[]
for i in range(0,v):
  x,y=map(float,input("Enter the coordinates").split())
  points.append((x,y))
print(points)  
frequency={}
for i in points:
  if i in frequency:
    frequency[i]+=1
  else:
    frequency[i]=1  
print(frequency)    