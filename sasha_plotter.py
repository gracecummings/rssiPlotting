import matplotlib.pyplot as plt
import matplotlib.dates as d
from datetime import datetime

f0 = open('HB08b_HBngCCM60_rssi_feb17-feb24.txt','r')
f1 = open('HE0_J16_2V5_12Feb.txt','r')
f0lines = f0.readlines()
f1lines = f1.readlines()

timestamps0 = []
vals0      = []
timestamps1 = []
vals1      = []

for line in f0lines:
    #print(line)
    splits = line.split()
    val   = float(splits[-1])
    #print(rssi)
    datetimebad = splits[0]+" "+splits[1]
    timestamp = datetime.strptime(datetimebad,"%d/%m/%Y %H:%M:%S")
    timestamps0.append(timestamp)
    vals0.append(val*1000)#*1000 for rssi

for line in f1lines:
    splits = line.split()
    val   = float(splits[-1])
    datetimebad = splits[0]+" "+splits[1]
    timestamp = datetime.strptime(datetimebad,"%d/%m/%Y %H:%M:%S")
    timestamps1.append(timestamp)
    vals1.append(val)

plt.plot(timestamps0,vals0,'bo-')#,'HE1 2.5V J15')
#plt.plot(timestamps1,vals1,'go-')#,'HE1 2.5V J16')
plt.ylabel("RSSI (mA)")
plt.ylim(0.1,0.4)
plt.xlabel("date+time")
plt.show()



