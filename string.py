
a=input("enter string")
n=len(a)
flag=0
b=0
d=0

for i in range (n):
    c=a[i]
    if(c=='0'or c=='1'or c=='2'or c=='3'or c=='4'or c=='5'or c=='6'or c=='7'or c=='8'or c=='9'):
        if(i==0):
            d=a[i]
        else:
            if (flag==1):
                d=d+a[i]
            else:
                d=a[i]
        flag=1         
    else:
        flag=0
        d=int(d)
        b=int(b) 
        if(d>b):
            b=d
print (b)          
    

