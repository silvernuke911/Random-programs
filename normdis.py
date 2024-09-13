from numpy import random
import matplotlib.pyplot as plt
import math as mt

def normal_dis_points(num,mean=0,stddev=1):
    output=[]
    for i in range(num):
        x=random.normal(mean,stddev)
        output.append(x)
    return output

def normal_dist_plot(samples,mean=0,stddev=1,offset=0,spread=[-5,5]):
    output1=[]
    step=(spread[1]-spread[0])/samples
    x=spread[0]-step
    for i in range(samples+1):
        x+=step
        output1.append(x)
    output2=[]
    for j in range(len(output1)):
        y=output1[j]
        z=(1/(mt.sqrt(2*mt.pi)*stddev))*mt.exp(-0.5*((y-offset)/stddev)**2)
        output2.append(z)
    return [output1,output2]
def plot():
    plt.axis([-5,5,-5,5])
    plt.grid()
    plt.scatter(list1,list2,marker=".")
    plt.show()
def vscal(constant,vector):
    output=[]
    for i in range(len(vector)):
        output.append(constant*vector[i])
    return output
n=100000
bin=100
list1=normal_dis_points(n)
list2=normal_dis_points(n)
listx=normal_dist_plot(n)[0]
listy=normal_dist_plot(n)[1]
print(listy)
listy=vscal(n*(8.5/bin),listy)
def histogram():
    plt.hist(list1,bins=bin)
    plt.plot(listx,listy)
    plt.grid()
    plt.show()
plot()
histogram()


def csv_opener(filepath):
    import csv
    with open(filepath, mode ='r')as file:
        csvFile = csv.reader(file)
        col_arr=[]
        for lines in csvFile:
            col_arr.append(lines)
    file.close()
    return col_arr

def txt_opener(filepath):
    with open(filepath, 'r') as file: 
        lines = file.readlines() 
        words= [line.strip() for line in lines]
    file.close()
    return words

col_arr=csv_opener(r'sinwav.csv')

def column_extractor(array,column):
    col=[]
    for i in range(len(array)):
        col.append(col_arr[i][column])
    return col

def float_converter(strlist):
    output=[]
    for strg in strlist:
        output.append(float(strg))
    return output

def column_show():
    col1=float_converter(column_extractor(col_arr,0))
    print(col1)
    col2=float_converter(column_extractor(col_arr,1))
    print(col2)
    plt.axis([-10,10,-1.5,1.5])
    plt.grid()
    plt.plot(col1,col2,marker=".",linestyle="")
    plt.show()

def r_squared(x_list,y_list,function):
    def ss_res(x_list,y_list,function):
        sum=0
        for i in range(len(x_list)):
            sum+=(y_list[i]-function(x_list[i]))**2
        return sum
    def ss_tot(y_list):
        ave=mean(y_list)
        sum=0
        for i in range(len(y_list)):
            sum+=(y_list[i]-ave)**2
        return sum
    def mean(nlist):
        sum=0
        for i in range(len(nlist)):
            sum+=nlist[i]
        return sum/len(nlist)
    rsqd=1-ss_res(x_list,y_list,function)/ss_tot(y_list)
    return rsqd

# def func(x):
#     return mt.sin(x)
# print(r_squared(col1,col2,func))

