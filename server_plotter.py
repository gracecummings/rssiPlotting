import matplotlib.pyplot as plt
import matplotlib.dates as d
from datetime import datetime
import numpy

def timeFromServer(outline):
    #stupid   = outline.split(" #get")
    timestamp = datetime.strptime(outline[0], "%Y-%m-%d %H:%M:%S")
    return timestamp

if __name__=='__main__':

    server_transcript = open("July21_notes.txt","r")
    transcript        = server_transcript.readlines()

    timep = []
    timer = []
    timet = []
    rssil = []
    templ = []
    pwr_stat = []
    link = "0"
    for line in transcript:
        if "#get HE{0}-bkp_pwr_bad".format(link) in line:
            if "#ERROR!!" in line:
                continue
            out   = line.split(" #get")
            timetemp = timeFromServer(out)
            timep.append(timetemp)
            #templ.append(float(temp))
            bit_str = out[-1]
            bitish = bit_str.split("#")[1]
            bit = int(bitish)
            pwr_stat.append(bit)
            #print(stupid)
        if "#get HE{0}-vtrx_rssi_J15_Cntrl_f_rr".format(link) in line:
            if "#ERROR!!" in line:
                continue
            #print(line)
            linelist = line.split()
            stupid   = line.split(" #get")
            timerssi = datetime.strptime(stupid[0], "%Y-%m-%d %H:%M:%S")
            rssi = float(linelist[-1])*1000
            timer.append(timerssi)
            rssil.append(rssi)
        if "#get HE{0}-temp_J15_Ctrl_U18_f_rr".format(link) in line:
            if "#ERROR!!" in line:
                continue
            out   = line.split(" #get")
            timetime = timeFromServer(out)
            timet.append(timetime)
            temppart = out[-1]
            temp = float(temppart.split('#')[-1].strip('\n'))
            templ.append(temp)
            
            
    timet_n = numpy.array(timet)
    timer_n = numpy.array(timer)
    rssil_n = numpy.array(rssil)
    templ_n = numpy.array(templ)

    std_rssi = numpy.std(rssil_n)
    print(std_rssi)

    #print(len(templ))
    #print(len(rssil))
    #print(len(timer))
    
    #print(timet)
    #print(pwr_stat)
    #print(templ)
    #plt.plot(timer,rssil,"o")
    #plt.ylabel("rssi (mA)")
    #plt.xlabel("date+time")
    #plt.show()
    mintime = min(timer)
    maxtime = max(timer)

    fig,(rssisub,pwrsub,tempsub) = plt.subplots(3,1,gridspec_kw={'height_ratios':[3,1,1]})
    rssisub.plot(timer,rssil,"-o")
    rssisub.set_ylabel("rssi mA")
    pwrsub.set_ylabel("bkp_pwr_bad")
    pwrsub.set_ylim(-.1,1.1)
    pwrsub.plot(timep,pwr_stat,'-o')
    pwrsub.set_xlim(mintime,maxtime)
    rssisub.set_xlim(mintime,maxtime)
    tempsub.plot(timet,templ)
    tempsub.set_xlim(mintime,maxtime)
    tempsub.set_ylabel("temp C")
    tempsub.set_xlabel("date+time")
    plt.show()

