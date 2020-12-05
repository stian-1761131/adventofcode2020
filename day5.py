d5input = []

with open('inputd5.txt','r') as f:
        inlines = f.readlines()
        for line in inlines :
            d5input.append(line.strip('\n'))


testStr = ['FBFBBFFRLR']

def getUpperHalf(bottom, top) :
    bottom1 = top - ((top - bottom) // 2)
    top1 = top
    return bottom1, top1

def getLowerHalf(bottom, top) :
    bottom1 = bottom
    top1 = top - ((top - bottom) // 2) - 1 

    return bottom1, top1

def getUpperLower(input) :
    theinput = input[:7]
    lowerBound = 0
    upperBound = 127
    for i in theinput :
        if i == 'F' :
            lowerBound, upperBound = getLowerHalf(lowerBound, upperBound)
        if i == 'B' :
            lowerBound, upperBound = getUpperHalf(lowerBound, upperBound)
    if input[6] == 'F' :
        return lowerBound
    else :
        return upperBound

def getRight(bottom, top) :
    bottom1 = top - ((top - bottom) // 2)
    top1 = top
    return bottom1, top1

def getLeft(bottom, top) :
    bottom1 = bottom
    top1 = top - ((top - bottom) // 2) - 1

    return bottom1, top1

def getLeftRight(input) :
    theinput = input[7:]
    lowerBound = 0
    upperBound = 7
    for i in theinput :
        if i == "L" :
            lowerBound, upperBound = getLeft(lowerBound, upperBound)
        if i == "R":
            lowerBound, upperBound = getRight(lowerBound, upperBound)

    if input[-1] == 'L':
        return lowerBound
    else :
        return upperBound

def getSeatID(rows, columns) :
    return (rows * 8) + columns

seatIDs = []

for j in d5input :
    rows = getUpperLower(j)
    columns = getLeftRight(j)
    seatIDs.append(int(getSeatID(rows, columns))) 

#The seats with +1seatID's and -1seatIDs will be on the list
seatIDs.sort()
for a in range(len(seatIDs)-1) :
    if (seatIDs[a]+1) != seatIDs[a+1] :
        print(seatIDs[a] + 1)