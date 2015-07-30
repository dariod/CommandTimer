#!/usr/bin/python
import subprocess
import time

numberOfTries=5
cmd=['/bin/sleep','2']




def avg(list):
    sum = 0
    for elm in list:
        sum += elm
    return(sum/(len(list)*1.0))

def min(list):
    min = list[0]
    for elm in list[1:]:
        if elm < min:
            min = elm
    return(min)
            
def max(list):
    max = list[0]
    for elm in list[1:]:
        if elm > max:
            max = elm
    return(max)

elapsedTimes=[]
for i in range(numberOfTries):
    print "Iteration %d..." % (i)
    try:
        startTime=time.time()
        cmdHandle=subprocess.Popen(cmd,shell=False,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    except OSError:
        print "Cannot exeucte %s" % (cmd)
        
    rtn=cmdHandle.wait()
    endTime=time.time()
    elapsedTimes.append(endTime - startTime)
    
print "Runtimes:"
print "Minimum: %8.4f" % (max(elapsedTimes))
print "Maximum: %8.4f" % (min(elapsedTimes))
print "Average: %8.4f" % (avg(elapsedTimes))
