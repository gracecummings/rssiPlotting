import matplotlib.pyplot as plt
import matplotlib.dates as d
import numpy as np
import pandas as pd
from datetime import datetime

def rssiIntToCurr(ival,val2v5):
    uampRSSI = ((val2v5*1024./2.5)-ival)*2.5/1024.*1000
    return uampRSSI

if __name__=="__main__":

    rbx = 14.

    #rssi txt needs processing to work. removes 'HEP' and 'HEM' from RBx and replaces with sign
    #col1 = unix timestamp, col2 = RBx number, col6 = 2.5V, col9 =  J14 RSSI int, col10 = J15 RSSI int
    data = np.loadtxt('rssi_Aug30_prepped.txt',usecols=(1,2,6,9,10))
    df   = pd.DataFrame(data)
    df["currJ14"] = rssiIntToCurr(df[3],df[2])#RSSI in uA
    df["currJ15"] = rssiIntToCurr(df[4],df[2])#RSSI in uA



    #Get RBx of choice, and have it with 2.5V active
    rbxinf = df[(df[1] == 14)]
    rbxon  = rbxinf[(rbxinf[2] > -1.)]
    timestamps = rbxon[0].tolist()
    #rtimestamps = list(map(lambda d : datetime.fromtimestamp(d).strftime("%y-%m-%d %H:%M:%S"),timestamps))
    rtimestamps = list(map(lambda d : datetime.fromtimestamp(d),timestamps))
    
    #plot
    fig,(rssi15,rssi14,vsub) = plt.subplots(3,1,gridspec_kw={'height_ratios':[3,3,1]})
    fig.set_figheight(8)
    fig.set_figwidth(6)
    rssi15.plot(rtimestamps,rbxon["currJ15"])
    rssi14.plot(rtimestamps,rbxon["currJ14"])
    vsub.plot(rtimestamps,rbxon[2])
    plt.show()



