import sys
import copy

#!/usr/bin/python3
def openFile():
    if(len(sys.argv) != 1):
        sys.exit(1)

    fname = input()
    try:
        dataFile = open(fname, "r")
        return dataFile
    except IOError:
        print("Invalid File Name")
        return 0


def parseFile(file):
    dataFile = openFile()
    c = dataFile.read(1)
    n = c
    counter = 1
    knightCounter = 0
    knights = {}
    ladies = {}
    knightPrefs = []
    ladiesPrefs = []


    while c and counter != ((2 * n * (n + 1)) / 2) + 1:
        counter += 1
        c = dataFile.read(1)
        #store knights

        if(c == '\n'):
            knightCounter += 1

    while c and counter != 2 * n * (n + 1) + 1:
        counter += 1
        #store ladies


def parseF():
    dataFile = openFile()
    line = dataFile.readline()
    line = line.strip()
    numKnights = line
    numKnights = int(numKnights)
    #knightPrefs = [] #the ladies that the knights prefer
    #ladiesPrefs = []
    counter = 1
    knights = {}
    ladies = {}

    for line in dataFile:
        line = line.strip()
        if counter < (numKnights + 1):
            knightPrefs = line.split(" ")
            tempDict = {knightPrefs[0] : knightPrefs[1:]}
            knights.update(tempDict)
        else:
            ladiesPrefs = line.split(" ")
            tempDict = {ladiesPrefs[0] : ladiesPrefs[1:]}
            ladies.update(tempDict)
        counter += 1
    dataFile.close()

    return knights, ladies


def isFree(people):
    for person in people:
        if people.pop(person[0]) == 0:
            return False
    return True


def galeShapley(knights, ladies):
    knightsList = knights.keys()
    ladiesList = ladies.keys()
    knightsValues = knights.values()
    #print(knightsValues)
    knightsMatchedList = {}
    ladiesMatchedList = {}

    for knight in knightsList:
        tempDict = {knight : 0}
        knightsMatchedList.update(tempDict)
    for lady in ladiesList:
        tempDict = {lady : 0}
        ladiesMatchedList.update(tempDict)
    #possible invariant: knightsMatchedList keys(knights)
    #are in the same order as the knights in the dictionary passed in
    while(isFree(knightsMatchedList)):
        m = knightsMatchedList.popitem()
        mPref = knights.popitem()
        preferenceList = mPref[1]
        if m[1] == 0:
            #get a lady, the highest lady that has not been proposed to
            for lady in preferenceList:
                if ladiesMatchedList.get(lady) == 0:
                    fiances = {m[0] : lady}
                    knightsMatchedList.update(fiances)
                    ladiesMatchedList.update(lady, m[0])
        else:
            prefLadyList = knights.get(m[1])
            #mprime = prefLadyList[]


        #put knight back in dictionary
        knights.update(mPref)



    return


def main():
    knights, ladies = parseF()
    galeShapley(knights, ladies)

main()