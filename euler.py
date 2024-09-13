#Prints the euler number progression
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def euler_num(y):
    sum=0
    for n in range(0,y+1):
        x=1/math.factorial(n)
        sum+=x
    return sum

def antiquity_pi(y):
    sum=0
    for n in range(1,y+1):
        x=((-1)**(n-1))/(2*n-1)
        sum+=x
    return 4*sum

def fizzbuzz(n):
    for i in range(1,n+1):
        if i%15==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)

def orderedlist(n):
    list=[]
    for i in range(1,n+1):
        list.append(i)
    return list

def shuffler(arr):
    import random
    for i in range(0,len(arr)-2):
        j=random.randint(i,len(arr)-1)
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
    return(arr)

def selectionSort(arr):
    n = len(arr)
    for step in range(n):
        min_idx = step
        for i in range(step + 1, n):
            if arr[i] < arr[min_idx]:
                min_idx = i
        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            print(arr)
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return arr
        
def leibnizPi(n):
    sum=0
    for k in range(0,n+1):
        x=((-1)**k)/(2*k+1)
        sum+=x
    return(4*sum)

def euler(n):
    sum=0
    for k in range(0,n+1):
        x=1/math.factorial(k)
        sum+=x
    return sum

def choose(n,k):
    v=math.factorial(n)/(math.factorial(n-k)*math.factorial(k))
    return v

def newtonPi1(n):
    sum=0
    for k in range(0,n+1):
        numerator=((-1)**(k-1))*math.factorial(2*k)
        denominator=(4**k)*(math.factorial(k)**2)*(2*k-1)
        xterm=((-1)**k)*(1/(2*k+1))
        sum+= xterm*(numerator/denominator)
        est=4*sum
        print(est)
    return est

def newtonPi2(n):
    import math
    sum=0
    for k in range(0,n+1):
        numerator=((-1)**(k-1))*math.factorial(2*k)
        denominator=(4**k)*(math.factorial(k)**2)*(2*k-1)
        xterm=((-1)**k)*((0.5)**(2*k+1)/(2*k+1))
        sum+= xterm*(numerator/denominator)
        est=12*(sum-(math.sqrt(3)/8))
        #print(est)
    return est




def Convergence_visualizer(const,func,num=100):
    def array_generate(num,func):
        x=np.array([])
        y=np.array([])
        for i in range(num+1):
            x=np.append(x,i)
            y=np.append(y,func(i))
            print(x[i],y[i])
        return x,y
    x,y=array_generate(num,func)
    z=x*0+const

    plt.plot(x,y,color='red')
    plt.plot(x,z,color='blue')
    plt.axis([0,num, np.min(y)-0.1, np.max(y)+0.1])
    plt.grid()
    plt.show()

Convergence_visualizer(np.pi,leibnizPi,20)