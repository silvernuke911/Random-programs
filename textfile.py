

import time

def int_list(num):
    i_list=[]
    for i in range(num):
        inte="1"
        for j in range(i):
            inte=inte+"0"
        i_list.append(int(inte))
    return i_list

def intlist(num):
    intlist=[]
    for i in range(0,num+1):
        intlist.append(i)

def time_def(numlist):
    for i in range(len(numlist)):
        start_time = time.time()
        intlist(numlist[i])
        elapsed_time=time.time() - start_time
        print(numlist[i],elapsed_time)
        file.write(str(numlist[i])+","+str(elapsed_time)+'\n')


def main():
    nlist=int_list(8)
    time_def(nlist)

    

file = open ('writeme.csv', 'w')
main() 
file.close()  