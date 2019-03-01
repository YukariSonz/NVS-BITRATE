import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from pandas import Series
import csv

def readLine(line):
    i=0
    while (line[i]!=" "):
        i=i+1
    i=i+1
    while (line[i]!=" "):
        i=i+1
    i=i+1
    timeStamp=""
    while (line[i]!=" "):
        timeStamp+=line[i]
        i=i+1
    res = int(timeStamp)
    return res

def writeCSV(toWrite, fileName):
    with open(fileName,"a") as writeFile:
        write = csv.writer(writeFile)
        write.writerows(toWrite)

def writeRes(toWrite,fileName):
    with open(fileName,"a") as writeFile:
        writeFile.write(toWrite)
        writeFile.write('\n')
    

file = open("WIN_20190224_10_03_59_Pro.mp4.txt","r")
line=file.readline()

fig, axs = plt.subplots()
axs.set_ylabel("Events of each frame")
axs.set_xlabel("Frame")
counter=0
numFrame=1
previous = 0
toPlot=[]
while line!='':
    now = readLine(line)
    line=file.readline()
    counter=counter+1
    if (now>previous+29000):
        #axs.scatter(numFrame,counter,s=10)
        toPlot.append(counter)
        counter=0
        numFrame=numFrame+1
    previous = now
series =Series(toPlot)
series.plot()
pyplot.show()

    
