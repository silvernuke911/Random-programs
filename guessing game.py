import math as mt
import random as rnd
def time_interval(time_start,time_end,step):
    steps=round((time_end-time_start)/step)
    time=time_start-step
    timelist=[]
    for i in range(0,steps+1):
        time+=step
        timelist.append(time)
    return(timelist)

def custom_sin(time,amplitude=1,phase=0):
    return amplitude*mt.sin(time-phase)




def main():
    timelist=time_interval(-10,10,0.1)
    for i in range(len(timelist)):
        print((str(timelist[i])+","+str(custom_sin(timelist[i]))))
        file.write(str(timelist[i])+','+str(custom_sin(timelist[i])+rnd.uniform(-0.1,0.1))+'\n')


file = open ('sinwav.csv', 'w')
main() 
file.close() 