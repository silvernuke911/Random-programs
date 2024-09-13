
def list_openfile(filepath):
    file_path=filepath
    with open(file_path, 'r') as file: 
        lines = file.readlines() 
        outputlist= [line.strip() for line in lines]
    return outputlist

def minutes_to_seconds(min_sec):
    colon=min_sec.index(":")
    mins=float(min_sec[0:colon])
    secs=float(min_sec[colon+1:len(min_sec)])
    return 60*mins+secs

def seconds_to_minutes(nsec,rnd=True):
    min=int(nsec//60)
    sec=nsec%60
    if rnd==True:
        sec=round(sec)
    if min<10:
        strmin="0"+str(min)
    else:
        strmin=str(min)
    if sec<10:
        strsec="0"+str(sec)
    else:
        strsec=str(sec)
    minsec=strmin+":"+strsec
    return minsec

def list_second_converter(minlist):
    output=[]
    for i in range(len(minlist)):
        output.append(minutes_to_seconds(minlist[i]))
    return output

#Statistical Shit
def sum(numlist):
    s=0
    for i in range(len(numlist)):
        s+=numlist[i]
    return s

def prod(numlist):
    p=1
    for i in range(len(numlist)):
        p*=numlist[i]
    return p

def mean(numlist):
    sum=0
    for i in range(len(numlist)):
        sum+=numlist[i]
    return sum/len(numlist)

def median(numlist):
    nlist=sorted(numlist)
    n=len(nlist)
    if n%2==0:
        return (nlist[n//2]+nlist[n//2-1])/2
    else:
        return nlist[n//2]

def mode(numlist):
    nlist=sorted(numlist)
    maxcount=0
    mode_list=[]
    for i in range(len(nlist)):
        count=0
        for j in range(i):
            if nlist[i]==nlist[j]:
                count+=1
        if count>maxcount:
            maxcount=count
            #modeval=nlist[i]
    if maxcount==0:
        return "No mode"
    for k in range(len(nlist)):
        count=0
        for l in range(k):
            if nlist[k]==nlist[l]:
                count+=1
        if count==maxcount:
            mode_list.append(nlist[k])
    if len(mode_list)==1:
        return mode_list[0]
    return mode_list

def geometric_mean(numlist):
    n=len(numlist)
    p=prod(numlist)
    return (p)**(1/n)

def harmonic_mean(numlist):
    n=len(numlist)
    s=0
    if 0 in numlist:
        return "Division by zero not allowed"
    for i in range(n):
        s+=(1/numlist[i])
    return n/s

def stddev(numlist):
    import math
    num_mean=mean(numlist)
    sum=0
    for i in range(len(numlist)):
        sum+=(numlist[i]-num_mean)**2
    return math.sqrt((sum)/len(numlist))

def list_csv(filepath):
    list_rows=list_openfile(filepath)
    output=[]
    for row in list_rows:
        rowlist=row.split(',')
        output.append(rowlist)
    return output
        
def column_list_csv(csv_list,column_name):
    for item in csv_list[0]:
        if item==column_name:
            item_index=csv_list[0].index(item)
    output=[]
    for i in range(1,len(csv_list)):
        output.append(csv_list[i][item_index])
    return output
    
def minutes_average(time_list):
    def remove_items(test_list, item): 
        res = [i for i in test_list if i != item] 
        return res 
    newlist=remove_items(time_list,'N/A')
    seclist=list_second_converter(newlist)
    sec_average=mean(seclist)
    return seconds_to_minutes(sec_average)

def minutes_stddev(time_list):
    def remove_items(test_list, item): 
        res = [i for i in test_list if i != item] 
        return res 
    newlist=remove_items(time_list,'N/A')
    seclist=list_second_converter(newlist)
    sec_stddev=stddev(seclist)
    return seconds_to_minutes(sec_stddev)

filepath=r'tapa_results.csv'
csv_list=list_csv(filepath)
assembly_list=column_list_csv(csv_list,'ï»¿assembly')
balancing_list=column_list_csv(csv_list,'balancing')
alignment_list=column_list_csv(csv_list,'alignment')
overall_list=column_list_csv(csv_list,'overall')


for i in range(len(csv_list)-1):
    print(assembly_list[i],balancing_list[i],alignment_list[i],overall_list[i])
print()
print(minutes_average(assembly_list),minutes_average(balancing_list),minutes_average(alignment_list),minutes_average(overall_list))
print(minutes_stddev(assembly_list),minutes_stddev(balancing_list),minutes_stddev(alignment_list),minutes_stddev(overall_list))
print()

# times=list_openfile(r"C:\Users\verci\Downloads\overall_times.txt")
# seclist=list_second_converter(times)
# print(times)
# print(seclist)
# print(seconds_to_minutes(average(seclist)))
# print(seconds_to_minutes(stddev(seclist)))
    # print(sum(nlist), ":", prod(nlist))
    # print(prod(nlist))
    # print(mean(nlist))
    # print(median(nlist))
    # print(mode(nlist))
    # print(geometric_mean(nlist))
    # print(harmonic_mean(nlist))

# nlist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,345,456,47,5687,67,9,573,56,24,51,351,34,12,45356,45,75,68,875867,867,978,9546,7356,3243,12412,31242,34,254,3456,4567,568,624,524,5,3453,46,45,75,67,35,62,45,23,5434,64,7,5687,45,63,4542,45]

# def main(n):
#     # nlist=[]
#     # for i in range(n):
#     #     nlist.append(i)
#     # return nlist

#     for i in range(n):
#         print(i)
#     return(i+1)



# import time
# start_time = time.time()
# print(main(10000))
# print(time.time() - start_time, "seconds")

# # Opening a file 'example.txt'  
# file = open("example.txt", "w")  

def binary_searcher(guess,number,min,max):
    minnum=min
    maxnum=max
    i=0
    print(minnum,guess,number,maxnum,i)
    while guess!=number:
        if guess<number:
            minnum=guess
        elif guess>number:
            maxnum=guess
        guess=(minnum+maxnum)//2
        i+=1
        print(minnum,guess,number,maxnum,i)
    
binary_searcher(0,99999,0,100000)

