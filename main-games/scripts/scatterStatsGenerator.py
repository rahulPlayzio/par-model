import sys
import utility
import fileSystemManager
import gameDataMediator

CONST_REEL_ROWS      = 3
CONST_SCATTER_SYMBOL = 'Scatter'

def GetScatterHitDict(_gameName):
  scatterHitDict        = {}
  scatterKeyList        = gameDataMediator.GetScatterKeyList(_gameName)
  scatterHitDict[scatterKeyList[0]] = Get3xScatterHitCount(_gameName)
  scatterHitDict[scatterKeyList[1]] = Get4xScatterHitCount(_gameName)
  scatterHitDict[scatterKeyList[2]] = Get5xScatterHitCount(_gameName)
  return scatterHitDict

def GetReelStripLenList(_gameName):
  reelKeysList      = gameDataMediator.GetReelKeyList(_gameName)
  reelStripsDict    = gameDataMediator.GetReelStripsDict(_gameName)
  reelStripsLenList = [len(reelStripsDict[reelKey]) for reelKey in reelKeysList]
  return reelStripsLenList

def GetScatterSymbolCountList(_gameName):
  reelKeysList      = gameDataMediator.GetReelKeyList(_gameName)
  reelStripsDict    = gameDataMediator.GetReelStripsDict(_gameName)
  scatterCountList  = [reelStripsDict[reelKey].count(CONST_SCATTER_SYMBOL) for reelKey in reelKeysList]
  return scatterCountList

def GetScatterCountForCombo(_hitIndexList, _reelLength, _gameName):
  hitCount          = 1
  scatterCountList  = GetScatterSymbolCountList(_gameName)
  reelStripsLenList = GetReelStripLenList(_gameName)
  for index in range(_reelLength):
    if index in _hitIndexList:
      hitCount *= (scatterCountList[index] * CONST_REEL_ROWS)
    else:
      hitCount *= (reelStripsLenList[index] - (scatterCountList[index] * CONST_REEL_ROWS))
  return hitCount

def Get3xScatterHitCount(_gameName):
  scatterCount    = 0
  reelKeysList    = gameDataMediator.GetReelKeyList(_gameName)

  reelLength      = len(reelKeysList)
  indexList1      = [index for index in range(reelLength)]

  for index1 in indexList1:
    indexList2         = indexList1[index1 + 1:]
    for index2 in indexList2:
      indexList3       = indexList1[index2 + 1:]
      for index3 in indexList3:
        hitIndexList   = [index1, index2, index3]
        scatterCount  += GetScatterCountForCombo(hitIndexList, reelLength, _gameName)

  return scatterCount

def Get4xScatterHitCount(_gameName):
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
          hitIndexList   = [index1, index2, index3, index4]
          scatterCount  += GetScatterCountForCombo(hitIndexList, reelLength, _gameName)

  return scatterCount

def Get5xScatterHitCount(_gameName):
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
            hitIndexList   = [index1, index2, index3, index4, index5]
            scatterCount  += GetScatterCountForCombo(hitIndexList, reelLength, _gameName)

  return scatterCount

def GetTotalComboCounts(_gameName):
  reelLengthList    = GetReelStripLenList(_gameName)
  totalCombos       = 1
  for reelLength in reelLengthList:
    totalCombos    *= reelLength
  return totalCombos

def GetScatterHitRatio(_gameName, _scatterHitDict, _totalCombos):
  scatterHitRatio       = {}
  scatterKeyList        = gameDataMediator.GetScatterKeyList(_gameName)
  for scatterKey in scatterKeyList:
    scatterHitRatio[scatterKey] = float(_scatterHitDict[scatterKey]) / _totalCombos
  return scatterHitRatio

def GetScatterHitRatioSum(_gameName, _scatterHitRatioDict):
  scatterHitRatioSum    = 0
  scatterKeyList        = gameDataMediator.GetScatterKeyList(_gameName)
  for scatterKey in scatterKeyList:
    scatterHitRatioSum += _scatterHitRatioDict[scatterKey]
  return scatterHitRatioSum

def GetScatterFrequencyDict(_gameName, _scatterHitRatioDict):
  scatterFrequencyDict  = {}
  scatterKeyList        = gameDataMediator.GetScatterKeyList(_gameName)
  for scatterKey in scatterKeyList:
    scatterFrequencyDict[scatterKey] = 1.0 / _scatterHitRatioDict[scatterKey]
  return scatterFrequencyDict  

def GetScatterFrequency(_scatterHitRatioSum):
  scatterFrequency      = 1.0 / _scatterHitRatioSum
  return scatterFrequency

def GetScatterPayFactorDict(_gameName, _scatterHitRatioDict):
  scatterFreeSpinsDict  = gameDataMediator.GetScatterFreeSpinDict(_gameName)
  scatterPayFactorDict  = {}
  scatterKeyList        = gameDataMediator.GetScatterKeyList(_gameName)
  for keyVar in scatterKeyList:
    scatterPayFactorDict[keyVar] = _scatterHitRatioDict[keyVar] * scatterFreeSpinsDict[keyVar]
  return scatterPayFactorDict

def GetPayFactorSum(_gameName, _scatterPayFactorSum):
  scatterPayFactorSum    = 0
  scatterKeyList         = gameDataMediator.GetScatterKeyList(_gameName)
  for keyVar in scatterKeyList:
    scatterPayFactorSum += _scatterPayFactorSum[keyVar]
  return scatterPayFactorSum

def GenerateScatterMultiplier(_gameName):
  scatterHitDict        = GetScatterHitDict(_gameName)
  totalCombos           = GetTotalComboCounts(_gameName)
  scatterHitRatioDict   = GetScatterHitRatio(_gameName, scatterHitDict, totalCombos)
  scatterPayFactorDict  = GetScatterPayFactorDict(_gameName, scatterHitRatioDict)
  scatterPayFactorSum   = GetPayFactorSum(_gameName, scatterPayFactorDict)
  scatterMultiplier     = 1.0 / (1- scatterPayFactorSum)
  return scatterMultiplier

def main(_gameNo):
  gameName              = utility.GetGameName(_gameNo)

  scatterHitDict        = GetScatterHitDict(gameName)
  totalCombos           = GetTotalComboCounts(gameName)
  scatterHitRatioDict   = GetScatterHitRatio(gameName, scatterHitDict, totalCombos)
  scatterHitRatioSum    = GetScatterHitRatioSum(gameName, scatterHitRatioDict)
  scatterFrequencyDict  = GetScatterFrequencyDict(gameName, scatterHitRatioDict)
  scatterFrequency      = GetScatterFrequency(scatterHitRatioSum)
  scatterPayFactorDict  = GetScatterPayFactorDict(gameName, scatterHitRatioDict)
  scatterPayFactorSum   = GetPayFactorSum(gameName, scatterPayFactorDict)
  scatterMultiplier     = GenerateScatterMultiplier(gameName)

  scatterStatsStr                         = {}
  scatterStatsStr['scatterHitDict']       = scatterHitDict
  scatterStatsStr['totalCombos']          = totalCombos
  scatterStatsStr['scatterHitRatioDict']  = scatterHitRatioDict
  scatterStatsStr['scatterHitRatioSum']   = scatterHitRatioSum
  scatterStatsStr['scatterFrequencyDict'] = scatterFrequencyDict
  scatterStatsStr['scatterFrequency']     = scatterFrequency
  scatterStatsStr['scatterPayFactorDict'] = scatterPayFactorDict
  scatterStatsStr['scatterPayFactorSum']  = scatterPayFactorSum
  scatterStatsStr['scatterMultiplier']    = scatterMultiplier

  print 'scatterFrequency      ', scatterFrequency
  print 'scatterMultiplier     ', scatterMultiplier, '\n'

  fileSystemManager.createScatterStatsDict(gameName, scatterStatsStr)

if __name__ == "__main__":
  main(sys.argv[1])