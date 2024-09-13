greeting='Hello World!'
Username="Silvernuke"
print(greeting)
print(Username)
# a=2
# b=3
# c=a+b
# print(c)

firstname="Vercil"
lastname="Juan"
fullname=f"{firstname} {lastname}"
print(fullname)

list1=[1,2,3,4,5]

print(list1[0])
print(type(list1[0]))

list2=["I","am","an","Idiot"]
list3=["Good","you","know"]

list2.extend(list3)
print(list2)
list2.append(list3)
print(list2)

list2.insert(4,"hahahha")
print(list2)
#.extend - adds two lists
#.append - appends at the last index
#.index - determines the index
#.pop - remove from the index
#.count - count the number of data
#.insert - inserts data at an index



# numlist=[1,4,53,23,5,6]
# numlist.sort()
# print(numlist)


def orderedlist(y):
    list=[]
    for i in range(1,y+1):
        list.append(i)
    return list

print(orderedlist(10))
    


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

import random
print(random.randint(0,90))

def orderedlist(y):
    list=[]
    for i in range(1,y+1):
        list.append(i)
    return list

arr=orderedlist(20)
print(arr)

def shuffler(arr):
    for i in range(0,len(arr)-2):
        j=random.randint(i,len(arr)-1)
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
    return(arr)

print(shuffler(arr))
print(bubbleSort(arr))

input('Press ENTER to exit')
# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]
# print("Sorted array is:")
# for i in range(len(arr)):
#     print("% d" % arr[i], end=" ")


#