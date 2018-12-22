#rotate the elements of a matrix in clockwise direction

import pdb
b=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in  range(3):
        print (b[i][j]," ",end='')
    print("")    
n=3       
a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in  range(3):
        print (a[i][j]," ",end='')
    print("")   
pdb.set_trace()     
for i in range (3):
    for j in range (3):
        if(i==0):
            if (j==2):
                b[i+1][j]=a[i][j]
            else :
                b[i][j+1]=a[i][j]
            
        if(i==2):
            if (j==0):
                b[i-1][j]=a[i][j]
            else :
                b[i][j-1]=a[i][j]
        if (j==0):
            if(i==0):
                b[i][j+1]=a[i][j]
            else :
                b[(i-1)][j]=a[i][j]
        if (j==2):
            if (i==2):
                b[i][(j-1)]=a[i][j]
            else :
                b[i+1][j]=a[i][j]
if (n%2==1):
    c=(n-1)/2
    c=int(c)
    b[c][c]=a[c][c]                   
print (b)                
                