import copy
startConfig = [3, 3, 3, 4]
winAmount   = [150, 250, 350, 650]

def getFileData(_fileName):
  fileObj = open(_fileName, 'r')
  fileStr = fileObj.read()
  fileObj.close()
  return fileStr

def createFile(_fileName, _fileStr):
  fileObj = open(_fileName, 'w')
  fileObj.write(_fileStr)
  fileObj.close()

def getNextTupple(_tupple, _index):
  newTupple         = copy.copy(_tupple)
  newTupple[_index] = _tupple[_index] - 1
  nextTupple        = sorted(newTupple[0:3])
  nextTupple.append(newTupple[3])
  return nextTupple

def getProbList(_leafList):
  probDict = {}
  for tupple in _leafList:
    if (0 not in tupple): continue
    prob = 1.0
    totalLen = float(startConfig[0] + startConfig[1] + startConfig[2] + startConfig[3])
    for index in range(len(tupple)):
      multFactor = startConfig[index] - tupple[index]
      for j in range(multFactor):
        prob *=  (startConfig[index] - j) / totalLen
        totalLen -= 1
    probDict[str(tupple)] = prob
  return probDict

def getWeightedProbDict(_probDict, _leafDict):
  weightedProbDict = {}
  for dictKey in _leafDict:
    weightedProbDict[dictKey] = round((_probDict[dictKey] * _leafDict[dictKey]), 4)
  return weightedProbDict

def getweightedPayList(_itemProb3x, _itemProb4x):
  itemProbList = [_itemProb3x / 3, _itemProb3x / 3, _itemProb3x / 3, _itemProb4x]
  weightedPayList = [0, 0, 0, 0]
  for index in range(len(itemProbList)):
    weightedPayList[index] = winAmount[index] * itemProbList[index]
  return weightedPayList

def getAvgPay(_itemProb3x, _itemProb4x):
  weightedPayList = getweightedPayList(_itemProb3x, _itemProb4x)
  avgPay = 0.0
  for weightedPay in weightedPayList: avgPay += weightedPay
  return avgPay

def main():
  tuppleList = []
  countDict  = {}
  fileStr    = ''
  itemProb3x = 0.0
  itemProb4x = 0.0


  tuppleList.append(startConfig)
  countDict[str(startConfig)] = 1

  print tuppleList, '\n'
  print countDict, '\n'
  
  for i in range(10):
    newTuppleList = []
    leafDict   = {}
    newCountDict = {}
    for tupple in tuppleList:
      for index in range(len(tupple)):
        nextTupple      = getNextTupple(tupple, index)
        nextTuppleKey   = str(nextTupple)
        parentTuppleKey = str(tupple)
        if (nextTupple in newTuppleList):
          newCountDict[nextTuppleKey] = countDict[parentTuppleKey] + newCountDict[nextTuppleKey]
        else:
          newTuppleList.append(nextTupple)
          newCountDict[nextTuppleKey] = countDict[parentTuppleKey]

    tuppleList = []
    leafList   = []
    countDict  = {}
    for tupple in newTuppleList:
      tuppleKey           = str(tupple)
      if ( 0 in tupple):
        leafList.append(copy.copy(tupple))
        leafDict[tuppleKey]  = copy.copy(newCountDict[tuppleKey])
      else:
        countDict[tuppleKey] = copy.copy(newCountDict[tuppleKey])
        tuppleList.append(tupple)

    probDict         = getProbList(leafList)
    weightedProbDict = getWeightedProbDict(probDict, leafDict)

    for leaf in leafList:
      if (leaf[3] == 0): itemProb4x += weightedProbDict[str(leaf)]
      else:              itemProb3x += weightedProbDict[str(leaf)]


    fileStr  += 'Iteration        '+ str(i + 1) + '\n.................\n'
    fileStr  += 'tuppleList       '+ str(tuppleList)         + '\n'
    fileStr  += 'countDict        '+ str(countDict)          + '\n'
    fileStr  += 'leafDict         '+ str(leafDict)           + '\n'
    fileStr  += 'probDict         '+ str(probDict)           + '\n'
    fileStr  += 'weightedProbDict '+ str(weightedProbDict)   + '\n\n'

  avgPay          = getAvgPay(itemProb3x, itemProb4x)
  weightedPayList = getweightedPayList(itemProb3x, itemProb4x)

  fileStr  += 'itemProb3x      '+ str(itemProb3x/3.0)          + '\n'
  fileStr  += 'itemProbAll3x   '+ str(itemProb3x)              + '\n'
  fileStr  += 'itemProb4x      '+ str(itemProb4x)              + '\n'
  fileStr  += 'sumProb         '+ str(itemProb3x + itemProb4x) + '\n\n'
  fileStr  += 'weightedPayList '+ str(weightedPayList)         + '\n'
  fileStr  += 'avgPay          '+ str(avgPay)                  + '\n\n'

  createFile('stats', fileStr)
  print 'itemProb3x      '+ str(itemProb3x/3)    + '\n'
  print 'itemProbAll3x   '+ str(itemProb3x)      + '\n'
  print 'itemProb4x      '+ str(itemProb4x)      + '\n'
  print 'sumProb         '+ str(itemProb3x       + itemProb4x)   + '\n'
  print 'weightedPayList '+ str(weightedPayList) + '\n'
  print 'avgPay          '+ str(avgPay)          + '\n\n'

if __name__ == "__main__":
  main()