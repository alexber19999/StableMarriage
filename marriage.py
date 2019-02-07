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
        if people.get(person) == 0:
            return True
    return False


def galeShapley(knights, ladies):
    knightsList = knights.keys()
    ladiesList = ladies.keys()
    knightsValues = knights.values()
    #print(knightsValues)
    knightsMatchedList = {}
    ladiesMatchedList = {}

    M = []
    for knight in knightsList:
        tempDict = {knight : 0}
        knightsMatchedList.update(tempDict)
    for lady in ladiesList:
        tempDict = {lady : 0}
        ladiesMatchedList.update(tempDict)

    #possible invariant: knightsMatchedList keys(knights)
    #are in the same order as the knights in the dictionary passed in
    while(isFree(knightsMatchedList)):
        knightsMatchedListList = list(knightsMatchedList)
        m = knightsMatchedList.popitem()
        mPref = knights.popitem()
        preferenceList = mPref[1]
        if m[1] == 0:
            #get a lady, the highest lady that has not been proposed to
            for lady in preferenceList:
                if ladiesMatchedList.get(lady) == 0:
                    #add unordered map
                    fiances = {m[0] : lady}
                    match = m[0], lady
                    M.append(match)
                    print(match)
                    knightsMatchedList.update(fiances)
                    #ladiesMatchedList.update({lady, m[0]})
        else:
            #prefLadyList = knights.get(m[1])
            #mprime = prefLadyList[]
            mprime = knightsMatchedListList.index(mPref)
            if ladies[mPref][knightsMatchedListList.index(m[0])] < ladies[mPref][mprime]:
                ladiesMatchedList.update({knightsMatchedListList.index(mPref)})
                knightsMatchedList.update({mprime, 0})
                M.remove(mprime)
                match = ladies[mPref][knightsMatchedListList.index(m[0])] , ladies[mPref]
                M.append(match)

            else:
                knightsMatchedList.update(knightsMatchedListList.index(m[0]))
        #put knight back in dictionary
        knights.update(mPref)
    return M


def main():
    knights, ladies = parseF()
    knights = galeShapley(knights, ladies)
    #print()
    #print(knights)
main()