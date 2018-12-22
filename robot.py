#the directions are given to a robot to move from origin . calculate distance of final possision from origin to the nearest possible integer.
import math
n=int(input("how many directions you want to give ?"))
print('''Enter directions as UP,DOWN,RIGHT,LEFT and then steps with a space
         eg. UP 3''')
a=[]
for i in range (n):
    d=input("Enter direction").split(" ")
    a.append(d)
print (a)    
sumv=0
sumh=0    

for i in range (n):
    if(a[i][0]=='UP'):
        v=int(a[i][1])
        sumv=sumv+v
    if(a[i][0]=='DOWN'):
        v=int(a[i][1])
        sumv=sumv-v
    if (a[i][0]=='RIGHT'):
        h=int(a[i][1])
        sumh=sumh+h
    if (a[i][0]=='LEFT'):
        h=int(a[i][1])
        sumh=sumh-h
sumh=sumh*sumh
sumv=sumv*sumv
ans=sumv+sumh
ans=math.sqrt(ans)
round(ans)
ans=int(ans)
print(ans)        
        


