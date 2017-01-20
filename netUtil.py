#!/usr/bin/python
import os
#import sys
import csv
import datetime
import time
import subprocess as sp


class netUtil:

    def ping(self,ip):
        rcode=sp.Popen(["ping",ip,"-c1"],stdout=sp.PIPE).wait()
        if rcode==0:
		return True
    	else:
		return False
    	
            
    def pingMAC(self,MAC):
	output=sp.Popen(["arp"],stdout=sp.PIPE)
	for txt in output.communicate()[0].split('\n'):
		if MAC in txt:
			return self.ping(txt.split(" ")[0])
			
