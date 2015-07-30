#!/usr/bin/python
import subprocess
import time
import signal
import sys

numberOfTries=5
cmds=[['/bin/sleep','2'],
    ['/bin/sleep','1'],
    ['/bin/sleep','3']
    ]

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

for cmd in cmds:
    elapsedTimes=[]
    for i in range(numberOfTries):
        try:
            startTime=time.time()
            cmdHandle=subprocess.Popen(cmd,shell=False,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            
            cmdHandle.communicate()
            endTime=time.time()
            elapsedTimes.append(endTime - startTime)
            
        except KeyboardInterrupt:
            sys.stderr.write("Received Ctrl-C\n")
            cmdHandle.kill()
            break
        except OSError:
            sys.stderr.write("Cannot execute %s" % (cmd))
        except:
            sys.stderr.write("Problems executing %s" % (cmd))
        
    sys.stdout.write("Runtimes summary for %d runs of %s:\n" % (len(elapsedTimes)," ".join(cmd)))
    sys.stdout.write("Minimum: %8.4fs\n" % (min(elapsedTimes)))
    sys.stdout.write("Maximum: %8.4fs\n" % (max(elapsedTimes)))
    sys.stdout.write("Average: %8.4fs\n" % (avg(elapsedTimes)))
