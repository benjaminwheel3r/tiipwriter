# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 21:26:46 2016
@author: Ben
"""
import tiipWriter
from add import ThatGuy
import multiprocessing
from time import sleep

if __name__ == '__main__':
        #number of time increments script needs to run        
        n = 60
        dir = "C:\\Temp\\crapfolder\\twiitlog"
        list = []
        print "preloading logs"
        t = 1
        ThatGuy(n,dir,list)
        
        for a in list:
            print "Collecting Tweets....."
            p = multiprocessing.Process(target=tiipWriter.tiipWriter,args = (a,))
            p.start()
            try:
                p.join(18)
            except:
                sleep(2**t)
                t=t+1
            if p.is_alive():
                print " \n Saving Twitter Stream log   @  " + str(a)
                p.terminate()
                p.join(10)
            a = open(a,'r')
            a.close()
            if a.closed == True:
                print "File successfully closed"
            else: a.close()
            print "jamaica"