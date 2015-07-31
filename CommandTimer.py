#!/usr/bin/python
import subprocess
import time
import signal
import sys

numberOfTries=2
cmds=[['/bin/sleep','1'],
    ['/bin/sleep','1'],
    ['/bin/sleep','1']
    ]

class xList():

    def __init__(self):
        self._list=[]
        self._min=0
        self._max=0
        self._avg=0
        self._sum=0
        
    def append(self,v):
        self._list.append(v)
        self._max=max([self._max,v])
        self._min=min([self._min,v])
        self._sum+=v
        self._avg=(self._sum/len(self._list)*1.0)
        
    def getmin(self):
        return(self._min)
        
    def getmax(self):
        return(self._max)
        
    def getavg (self):
        return(self._avg)
        
    def __len__(self):
        return(len(self._list))
            
    def clear(self):
        self.__init__()
     
elapsedTimes=xList()
for cmd in cmds:
    elapsedTimes.clear()
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
            sys.stderr.write("Cannot execute %s\n" % (cmd))
            
        except:
            sys.stderr.write("Problems executing %s\n" % (cmd))
        
    sys.stdout.write("Runtimes summary for %d runs of %s:\n" % (len(elapsedTimes)," ".join(cmd)))
    sys.stdout.write("Minimum: %8.4fs\n" % (elapsedTimes.getmin()))
    sys.stdout.write("Maximum: %8.4fs\n" % (elapsedTimes.getmax()))
    sys.stdout.write("Average: %8.4fs\n" % (elapsedTimes.getavg()))
