import math as mt
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
    print("x")

main()