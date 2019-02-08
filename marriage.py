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

    return knights, ladies, numKnights


def isFree(people):
    for person in people:
        if people[person][0] == 0:
            return True
    return False





def galeShapley(knights, ladies, numKnights):

    knightsList = list(knights.keys())
    ladiesList = list(ladies.keys())
    #print(knightsValues)
    knightsMatchedList = {}
    ladiesMatchedList = {}

    M = {}
    for knight in knightsList:
        tempDict = {knight : [0, -1]}
        knightsMatchedList.update(tempDict)
    for lady in ladiesList:
        tempDict = {lady : [0, ladies[lady][0]]}
        ladiesMatchedList.update(tempDict)

    print(knightsMatchedList)
    print(ladiesMatchedList)
    #possible invariant: knightsMatchedList keys(knights)
    #are in the same order as the knights in the dictionary passed in

    while len(M) != numKnights:
        for m in knightsList:
            #get single dictionary entry for the knight m
            #knightIndex = knightsList.index(m)
            #tempDict = dict.fromkeys(knightsMatchedList[knightIndex])

            #get the first lady that the knight m has not proposed to
            ladyIndex = knightsMatchedList[m][1] + 1
            ladyName = ladiesList[ladyIndex]

            #finding if firstLady is free(0 for free, otherwise not free)
            #firstLadyFree = knightsMatchedList[m][0]
            #getting the name of the first lady not proposed to

            if ladiesMatchedList[ladyName][0] == 0:
                #add to the matched list
                M[ladyName] = m
                #add to the ladiesMatchedList
                ladiesMatchedList[ladyName][0] = 1
                #add to the knightsMatchedList
                #knightsMatchedList[m][0] = 1
                # increment ladyFreeIndex
                knightsMatchedList[m][1] += 1
            elif ladies[ladyName].index(M[ladyName]) < ladies[ladyName].index(m):
                #remove current from MatchedList
                v = M.pop(ladyName)
                #add the preferred to MatchList
                M[ladyName] = m
                #knightsMatchedList[m][0] = 0


    return M








def main():
    knights, ladies, numKnights = parseF()
    knights = galeShapley(knights, ladies, numKnights)
    print(knights)
main()