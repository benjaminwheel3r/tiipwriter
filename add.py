# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 18:43:56 2016

@author: Ben
"""
from os.path import exists

n = 5
dir = "C:\\Temp\\crapfolder\\twiitlog"
list = []

def ThatGuy(n,dir,list):
    #ThatGuy aka the One Up-er
    for i in range(n):
        logi = dir+str(i)
        if i == 0:
            while exists(logi+'.txt') == True:
                i=i+1
                logi = dir+str(i)
                #print logi
                k = i
            list.append(logi+'.txt')
            logi = dir+str(i)
            #print "#### preloading logs"
            k = i
        else:
            k= k+1
            logi = dir+str(k)
            list.append(logi+'.txt')
            #number of time increments script needs to run
    print("logs loaded")

if __name__ == '__main__':
    ThatGuy(n,dir,list)
    print(list)