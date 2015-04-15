import sys
import utility
import gameDataMediator

CONST_REEL_ROWS      = 3

def GetScatterHitDict(_gameName, _symbol):
  scatterHitDict        = {}
  scatterKeyList        = gameDataMediator.GetScatterKeyList(_gameName)
  scatterHitDict['2']   = Get2xScatterHitCount(_gameName, _symbol)
  scatterHitDict['3']   = Get3xScatterHitCount(_gameName, _symbol)
  scatterHitDict['4']   = Get4xScatterHitCount(_gameName, _symbol)
  scatterHitDict['5']   = Get5xScatterHitCount(_gameName, _symbol)
  return scatterHitDict

def GetReelStripLenDict(_gameName):
  reelKeysList      = gameDataMediator.GetReelKeyList(_gameName)
  reelStripsDict    = gameDataMediator.GetReelStripsDict(_gameName)
  reelStripsLenDict = {}
  for reelKey in reelKeysList:
    reelStripsLenDict[reelKey] = len(reelStripsDict[reelKey])
  return reelStripsLenDict

def GetScatterSymbolCountList(_gameName):
  reelKeysList      = gameDataMediator.GetReelKeyList(_gameName)
  reelStripsDict    = gameDataMediator.GetReelStripsDict(_gameName)
  scatterCountList  = [reelStripsDict[reelKey].count(CONST_SCATTER_SYMBOL) for reelKey in reelKeysList]
  return scatterCountList

def GetScatterCountForCombo(_hitIndexList, _reelLength, _gameName, _symbol):
  hitCount          = 1
  scatterCountDict  = gameDataMediator.GetSymbolCountList(_gameName, _symbol)
  reelStripsLenDict = GetReelStripLenDict(_gameName)
  reelKeysList      = gameDataMediator.GetReelKeyList(_gameName)
  for reelKey in reelKeysList:
    if reelKey in _hitIndexList:
      hitCount *= (scatterCountDict[reelKey] * CONST_REEL_ROWS)
    else:
      hitCount *= (reelStripsLenDict[reelKey] - (scatterCountDict[reelKey] * CONST_REEL_ROWS))
  return hitCount

def Get2xScatterHitCount(_gameName, _symbol):
  scatterCount    = 0
  reelKeysList    = gameDataMediator.GetReelKeyList(_gameName)

  reelLength      = len(reelKeysList)
  indexList1      = [index for index in range(reelLength)]

  for index1 in indexList1:
    indexList2           = indexList1[index1 + 1:]
    for index2 in indexList2:
      hitIndexList   = [reelKeysList[index1], reelKeysList[index2]]
      scatterCount  += GetScatterCountForCombo(hitIndexList, reelLength, _gameName, _symbol)

  return scatterCount

def Get3xScatterHitCount(_gameName, _symbol):
  scatterCount    = 0
  reelKeysList    = gameDataMediator.GetReelKeyList(_gameName)

  reelLength      = len(reelKeysList)
  indexList1      = [index for index in range(reelLength)]

  for index1 in indexList1:
    indexList2           = indexList1[index1 + 1:]
    for index2 in indexList2:
      indexList3         = indexList1[index2 + 1:]
      for index3 in indexList3:
        hitIndexList   = [reelKeysList[index1], reelKeysList[index2], reelKeysList[index3]]
        scatterCount  += GetScatterCountForCombo(hitIndexList, reelLength, _gameName, _symbol)

  return scatterCount

def Get4xScatterHitCount(_gameName, _symbol):
  scatterCount    = 0
  reelKeysList    = gameDataMediator.GetReelKeyList(_gameName)

  reelLength      = len(reelKeysList)
  indexList1      = [index for index in range(reelLength)]

  for index1 in indexList1:
    indexList2           = indexList1[index1 + 1:]
    for index2 in indexList2:
      indexList3         = indexList1[index2 + 1:]
      for index3 in indexList3:
        indexList4       = indexList1[index3 + 1:]
        for index4 in indexList4:
          hitIndexList   = [reelKeysList[index1], reelKeysList[index2], reelKeysList[index3], reelKeysList[index4]]
          scatterCount  += GetScatterCountForCombo(hitIndexList, reelLength, _gameName, _symbol)

  return scatterCount

def Get5xScatterHitCount(_gameName, _symbol):
  scatterCount    = 0
  reelKeysList    = gameDataMediator.GetReelKeyList(_gameName)

  reelLength      = len(reelKeysList)
  indexList1      = [index for index in range(reelLength)]

  for index1 in indexList1:
    indexList2           = indexList1[index1 + 1:]
    for index2 in indexList2:
      indexList3         = indexList1[index2 + 1:]
      for index3 in indexList3:
        indexList4       = indexList1[index3 + 1:]
        for index4 in indexList4:
          indexList5       = indexList1[index4 + 1:]
          for index5 in indexList5:
            hitIndexList   = [reelKeysList[index1], reelKeysList[index2], reelKeysList[index3], reelKeysList[index4], reelKeysList[index5]]
            scatterCount  += GetScatterCountForCombo(hitIndexList, reelLength, _gameName, _symbol)

  return scatterCount

def GetTotalComboCounts(_gameName):
  reelLengthList    = GetReelStripLenDict(_gameName)
  totalCombos       = 1
  for keyVar in reelLengthList:
    totalCombos    *= reelLengthList[keyVar]
  return totalCombos

def GetScatterHitRatio(_gameName, _scatterHitDict, _totalCombos):
  scatterHitRatio       = {}
  scatterKeyList        = gameDataMediator.GetScatterKeyList(_gameName)
  for scatterKey in scatterKeyList:
    scatterHitRatio[scatterKey] = round((float(_scatterHitDict[scatterKey]) / _totalCombos), 7)
  return scatterHitRatio

def GetScatterHitRatioSum(_gameName, _scatterHitRatioDict, _symbol):
  scatterHitRatioSum    = 0
  scatterKeyList        = gameDataMediator.GetScatterKeyList(_gameName)
  symbolCountPay        = gameDataMediator.GetPayValueForSymbol(_gameName, _symbol)
  print symbolCountPay
  for scatterKey in scatterKeyList:
    if (symbolCountPay[scatterKey] != 0):
      scatterHitRatioSum += _scatterHitRatioDict[scatterKey]
  return scatterHitRatioSum

def GetScatterFrequencyDict(_gameName, _scatterHitRatioDict):
  scatterFrequencyDict  = {}
  scatterKeyList        = gameDataMediator.GetScatterKeyList(_gameName)
  for scatterKey in scatterKeyList:
    if _scatterHitRatioDict[scatterKey] != 0:
      scatterFrequencyDict[scatterKey] = round((1.0 / _scatterHitRatioDict[scatterKey]), 7)
    else:
      scatterFrequencyDict[scatterKey] = -1
  return scatterFrequencyDict  

def GetScatterFrequency(_scatterHitRatioSum):
  if _scatterHitRatioSum != 0:
    scatterFrequency      = 1.0 / _scatterHitRatioSum
  else:
    scatterFrequency  = -1
  return scatterFrequency


def main(_gameNo):
  gameName = utility.GetGameName(_gameNo)
  #print GetScatterHitDict(gameName, 'Scatter')
  #print GetScatterHitDict(gameName, 'Scatter')
  #print GetScatterHitDict(gameName, 'Scatter')
  #print GetScatterHitDict(gameName, 'Scatter')

if __name__ == "__main__":
  main(sys.argv[1])