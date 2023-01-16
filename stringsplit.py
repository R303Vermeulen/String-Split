import sys
import time
from typing import Optional
import math
from math import sqrt

Tabert = []

def splitter(sting, dict):
    for x in range(len(sting)):
        if x == 0:
            Tabert.append( (0,0) )
        else:
            addlist = []
            for elem in Tabert:
                s = elem[0]
                cursting = sting[s:x]
                if cursting in dict:
                    k = elem[1]
                    addelem = (x, k+1)
                    addlist.append(addelem)

            if len(addlist) > 0:
                minel = addlist[0]
                for elem in addlist:
                    if elem[1] < minel[1]:
                            minel = elem
                Tabert.append(minel)
    return 0



if __name__ == "__main__":
    inFile = open(sys.argv[1])
    instringList = inFile.readlines()
    bigstring = instringList[0]
    dictionary = []
    i = 1
    while i < len(instringList):
        ts = instringList[i]
        end = len(ts) - 1
        ds = ts[:end]
        dictionary.append(ds)
        i += 1

    #bend = len(bigstring)
    #bigstring = bigstring[:bend]
    ############################## big string and dictionary ready for input

    splitter(bigstring, dictionary)

    ############################## Tabert is ready for output
    bsend = len(bigstring) - 1
    printBS = bigstring[:bsend]

    onInBS = len(bigstring) - 1
    onInT = len(Tabert) - 1
    startOfString = Tabert[onInT][0]
    lookingFor = Tabert[onInT][1] - 1

    #print(Tabert)
    #print(onInBS, startOfString, lookingFor)

    if onInBS != startOfString:
        print('It is not possible to decode "' + printBS + '".')
    else:
        print('It is possible to decode "' + printBS + '":')
        stingList = []
        loopisgoing = 1
        while loopisgoing == 1:
            onInT -= 1
            currenTnum = Tabert[onInT][1]
            if(currenTnum == lookingFor):
                startOfString = Tabert[onInT][0]
                curSting = bigstring[startOfString:onInBS]
                stingList.append(curSting)
                onInBS = startOfString
                lookingFor -= 1

            if onInT == 0:
                loopisgoing = 0

        ihatenamingmylastvariableicanneverpick = len(stingList) - 1
        listPrintSting = ""
        listPrintSting += stingList[ihatenamingmylastvariableicanneverpick]
        while ihatenamingmylastvariableicanneverpick > 0:
            ihatenamingmylastvariableicanneverpick -= 1
            listPrintSting += " "
            listPrintSting += stingList[ihatenamingmylastvariableicanneverpick]

        print(listPrintSting)







    #print(bigstring[:bend])
    #for word in dictionary:
        #print(word)