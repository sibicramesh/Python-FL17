import collections


def calcCharFreq(scount):
    strList=[]
    while len(strList)<int(scount):
        s = input("Enter Character: ")
        freqs = collections.Counter(s)
        strList.append((s,freqs))
    return strList


def findLongWord(w):
    wlen = []
    for ew in w:
        wlen.append((len(ew), ew))
    wlen.sort()
    return wlen[-1][1]


def getFirstLast(maxLen):
    numList = []
    while len(numList) < int(maxLen):
        num = input("Enter number")
        numList.append(num)
    numList.sort()
    return numList[0], numList[-1]


def getStringProps(s):
    d = l = 0
    for w in s:
        if w.isdigit():
            d += 1
        elif w.isalpha():
            l += 1
    print("Letter Count:", l)
    print("Digit Count:", d)


print("CHARACTER FREQUENCY")
schar = input("Enter max string count: ")
print(calcCharFreq(schar))
print("*******************")
print("\n")
print("LONGEST WORD")
print(findLongWord(["Python", "Java", "Go"]))
print("************")
print("\n")
print("LETTERS AND DIGITS COUNT")
sstring = input("Enter string with some digits: ")
getStringProps(sstring)
print("************************")
print("\n")
print("FIRST AND LAST FROM LIST")
smaxlen = input("Enter max length of list: ")
print(getFirstLast(smaxlen))
print("************************")
