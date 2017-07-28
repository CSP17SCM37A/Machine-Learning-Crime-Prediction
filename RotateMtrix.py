
# coding: utf-8

# In[20]:

#!/usr/bin/python
import math

def rotate(mat):
    N = len(mat)
    
    for x in range(0, math.floor(N/2)):
       
        for y in range(x,N-x-1 ):
            
            temp = mat[x][y];
 
            #move values from right to top
            mat[x][y] = mat[y][N-1-x];
 
            # move values from bottom to right
            mat[y][N-1-x] = mat[N-1-x][N-1-y];
 
            # move values from left to bottom
            mat[N-1-x][N-1-y] = mat[N-1-y][x];
 
            # assign temp to left
            mat[N-1-y][x] = temp;
        
       
 
# 5x5 matrix
matrix = [
    [ 0, 1, 2, 3, 4],
    [ 5, 6, 6, 8, 9],
    [10,11,12,13,14],
    [15,16,17,18,19],
    [20,21,22,23,24]
]

rotate(matrix)
print(matrix) 


# In[353]:

import math

def market(a,b):
    if len(a)==1 and len(b)==1 :
        return 1.0;
    r1=1
    r2=len(b)
    c2=len(b[0])
    #print(r1,c1,r2,c2)
    h=1
    while h : 
        mult= [0.0,0.0]
        for i in range(r1 ):
            for j in range(c2): 
                #print("j",j)
                for k in range(r2):
                    #print("ak",a[k])
                    #print("bkj",b[k][j])
                    #print("k",k)
                    #mult[i][j] += a[k] * b[k][j];
                    #print(a[k],b[k][j])
                    mult[j]+=a[k]*b[k][j]
                    #mult[j]+=round(a[k],4) * round(b[k][j],4)
                    #mult[j]=round(mult[j],4)
                    #print("mj",mult[j])
            #print("m",mult)
       
        for i in range(r2 ): 
            if round(a[i],6)==round(mult[i],6) :
                h=0
                #print(round(a[i],6)," ----",round(mult[i],6))
           
        a=mult
        #print(a)
        
    #print("mult",mult)    
    for i in range(r2 ):
        mult[i]=round(mult[i],4)

    #print(mult)    
    return mult
    
    
a1 = [0.4,0.6]

b1 = [[0.8,0.2],
     [0.1,0.9]]  
a = [1.0]

b = [1.0]      
x=market(a,b)    
print("result is :",x)


# In[347]:

def sub_median(array, key):
    array = array[::-1]
    print("Array: ",array)
    #print("Key: ",key)
    #print("Index of first occurence of key: ",array.index(key))
    array[:] = [x for x in array if x<=key]
    #print(array)
    #slice_index = array.index(key)
    sub_array=array
    #sub_array = array[slice_index:]
    print("Subarray: ",sub_array)
    length=len(sub_array)
    print("Length: ", length)
    if length%2 == 0:
        print(sub_array[int(length/2)], sub_array[int(length/2) - 1])
        median = (sub_array[int(length/2)] + sub_array[int(length/2) - 1])/2
    else:
        print("Middle Element: ",int(length/2))
        median = sub_array[int(length/2)]

    print("Median: ",median)
    return median 


print(sub_median([2],2))

print(sub_median([5,4,3,2,1],2))
print(sub_median([15,14,12,9,8,5,4,2,1],7))

print(sub_median([5,4,3,2,2,2,2,1],2))

print(sub_median([5,4,3,3,2,2,2,2,1,-10],3))


# In[169]:

import sys
def minSubArrayl(arrA,x):
    start = 0
    ansEnd = 0
    ansStart = 0
    currSum = 0
    pre=x
    n= len(arrA)
    for i in range(n+1 ):
        j=start
        while (currSum < x  and j<=len(arrA)): 
            #print(currSum)
            if x-currSum<pre and pre>0 and x-currSum >=0 :
                pre=x-currSum
                ansStart = i
                ansEnd = j
                #print(currSum,"   ",pre," ",i," ",j);
            if j>= len(arrA) :
                break;
            currSum = currSum +arrA[j]
            j=j+1
            start=j
            if j> len(arrA) :
                #print("hi",i," ",j)
                break;
        if i < len(arrA):
            currSum = currSum - arrA[i]

    #print("Minimum length of subarray to get1 ", x , " is : ", pre)
    #print("SubArray1 is:",ansStart," ",(ansEnd-1));
    #for i in range(ansStart,ansEnd ):
        #print("   ",arrA[i]);
    r1=[ansStart,(ansEnd-1)]    
    return r1

def minSubArray(arrA, x):
    start = 0
    ansEnd = 0
    ansStart = 0
    currSum = 0
    n= len(arrA)
    pos = sys.maxsize
    for i in range(n+1):
        while (currSum >= x):
            if currSum-x< pos :
                pos=currSum-x
                ansEnd = i
                ansStart = start
                #print(currSum,"   ",pos," ",i," ",start)
            currSum = currSum - arrA[start]
            start=start+1
        if i < len(arrA) :
            currSum = currSum + arrA[i]
    #print("Minimum length of subarray to get ", x , " is : ", minLen)
    #print("SubArray is:",ansStart," ",(ansEnd-1))
    #for i in range(ansStart,ansEnd ):
        #print("   ",arrA[i])
    r2=[ansStart,(ansEnd-1)]    
    return r2    




arra = [1,74,69,81,61,130,12]
arrb = [3,4,5,6,7]
arrc = [143,140]
if len(arrb) ==0:
    print(0) 
elif len(arrb)==1:
    print(arrc[0])
else:
    x=minSubArray(arrb,14)
    y=minSubArrayl(arrb,14)
    if x[1]==-1:
        print(y) 
    elif y[1]==-1:
        print(x)     
    elif x[1]>=y[1] :
        print(y)
    else:
        print(x)


# In[256]:

def drone_delivery(num_packages,delivery_Sequence):
    result=0
    if num_packages==0:
        return result
    
    s=1
    t=1
    b=delivery_Sequence[0]
    a=b.find('-')
    temp1=b[0:a]
    b=delivery_Sequence[num_packages-2]
    a=b.find('-')
    lastbutone=b[0:a]
    for j in range(num_packages):
        q=delivery_Sequence[j]
        a=q.find('-')
        gridn= q[0:a]
        if temp1!=gridn :
            temp2=gridn
            break
        else:
            temp2=0
    print(temp1,temp2)
    #print("first",temp)
   
    for i in range(num_packages):
        x=delivery_Sequence[i]
        #print(x)
        a=x.find('-')
        gridn= x[0:a]
        grid_num=x[a+1:]
        #print("grid",gridn,"grid_num",grid_num)
        if gridn==temp1:
            if()
            print(s,"grid",gridn,"grid_num",grid_num,"result",result)    
            while s < int(grid_num) :
                print(s,"s *********grid",gridn,"grid_num",grid_num,"result",result) 
                result=result+1
                s=s+1
                
            if (num_packages-1)==i:
                if lastbutone==gridn :
                    result=result+1
                    break
                else:
                    break
            result=result+1
            print(s,"s----------------------------------after grid",gridn,"result",result)    
        if gridn==temp2:
            print(t,"grid",gridn,"grid_num",grid_num,"result",result)       
            while t < int(grid_num) :
                print(t,"t *********grid",gridn,"grid_num",grid_num,"result",result)
                result=result+1
                t=t+1
                
            if (num_packages-1)==i:
                if lastbutone==gridn :
                    result=result+1
                    break
                else:
                    break
            result=result+1
            print(t,"t--------------------------------------After grid",gridn,"result",result)    
        #temp=[gridn,grid_num]    
        
        
    
    
    return result  
#delivery_Sequence=[]
delivery_Sequence = ["1234-1","1235-1","1235-3","1234-2"]
#delivery_Sequence = ["1234-1","1234-3","1234-6","1234-8"]
delivery_Sequence = ["1234-1","1235-3","1234-6","1235-8"]
#delivery_Sequence = ["1235-1","1235-4","1235-7","1235-10"]
num_packages=len(delivery_Sequence)
result=drone_delivery(num_packages,delivery_Sequence)
print(result)


# In[333]:

def drone_delivery(num_packages,delivery_Sequence):
    result=0
    if num_packages==0:
        return result
    
    s=1
    t=1
    y=0
    b=delivery_Sequence[0]
    a=b.find('-')
    w=b[0:a]
    
    temp1=[]
    temp2=[]
    for j in range(num_packages):
        q=delivery_Sequence[j]
        a=q.find('-')
        gridn= q[0:a]
        if w==gridn :
            temp1.append(q)
            
        else:
            y=gridn
            temp2.append(q)
    
   
    
    
    c=0
    d=0
    k=0
    for i in range(num_packages):
        x=delivery_Sequence[i]
        a=x.find('-')
        gridn= x[0:a]
        grid_num=x[a+1:]
        #print("grid",gridn,"grid_num",grid_num)
        if gridn==w:
            
            if d<len(temp2):
                b=temp2[d].find('-')
                k=(temp2[d])[b+1:]
                e=s
                #print(e ,int(grid_num),s," ",w)
                while(e < int(grid_num) and t< int(k)):
                    e=e+1
                    t=t+1
                #print(x,"s ",s,"t ",t)
            if x==temp1[c]:
                #print(s,"grid",gridn,"grid_num",grid_num,"result",result)    
                while s < int(grid_num) :
                    #print(s,"s *********grid",gridn,"grid_num",grid_num,"result",result) 
                    result=result+1
                    s=s+1
                
                
                result=result+1
                #print("t",t, s,"s----------------------------------after grid",gridn,"result",result)
                if d<len(temp2) and t < int(k):
                    t=t+1
                #print("t",t, s,"s----------------------------------after grid",gridn,"result",result) 
                c=c+1
        if gridn==y:
            if c<len(temp1):
                b=temp1[c].find('-')
                k=(temp1[c])[b+1:]
                e=t
                #print(e ,int(grid_num),s," ",w)
                while(e < int(grid_num) and s < int(k)):
                    e=e+1
                    s=s+1
                #print(x,"s ",s,"t ",t)
            if x==temp2[d]:
                #print(t,"grid",gridn,"grid_num",grid_num,"result",result)       
                while t < int(grid_num) :
                    #print(t,"t *********grid",gridn,"grid_num",grid_num,"result",result)
                    result=result+1
                    t=t+1
                
                result=result+1
                if c<len(temp1) and s < int(k):
                    s=s+1
                #print(t,"t--------------------------------------After grid",gridn,"result",result)    
                d=d+1
       
    return result  

delivery_Sequence=[]
num_packages=len(delivery_Sequence)
result=drone_delivery(num_packages,delivery_Sequence)
print(result)
delivery_Sequence = ["1234-1","1235-1","1235-3","1234-2"]
num_packages=len(delivery_Sequence)
result=drone_delivery(num_packages,delivery_Sequence)
print(result)
delivery_Sequence = ["1234-1","1234-3","1234-6","1234-8"]
num_packages=len(delivery_Sequence)
result=drone_delivery(num_packages,delivery_Sequence)
print(result)
delivery_Sequence = ["1234-1","1235-3","1234-6","1235-8"]
num_packages=len(delivery_Sequence)
result=drone_delivery(num_packages,delivery_Sequence)
print(result)
delivery_Sequence = ["1235-1","1235-4","1235-7","1235-10"]
num_packages=len(delivery_Sequence)
result=drone_delivery(num_packages,delivery_Sequence)
print(result)


# In[352]:

def  sub_median1(array, k):
    array[:] = [x for x in array if x<=k]
    print(array)
    length=len(array)
    if length==1:
        return array[0]
    if length%2 == 0:
        median = (array[int(length/2)] + array[int(length/2) - 1])/2
    else:
        median = array[int(length/2)]
    return median 

print(sub_median1([2],2))

print(sub_median1([5,4,3,2,1],2))
print(sub_median1([15,14,12,9,8,5,4,2,1],5))

print(sub_median1([5,4,3,2,2,2,2,1],2))

print(sub_median1([5,4,3,3,2,2,2,2,1,-10],3))


# In[ ]:



