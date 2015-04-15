import sys
import utility
import fileSystemManager
import gameDataMediator


CONST_BONUS_2X    = '2'
CONST_BONUS_3X    = '3'
CONST_BONUS_4X    = '4'
CONST_BONUS_5X    = '5'
CONST_BONUS_SYMBOL = 'Bonus'

def BonusInGame(_gameName):
  bonusInGame = utility.IsSymbolInReels(_gameName, CONST_BONUS_SYMBOL)
  return bonusInGame

def GetBonusHitDict(_gameName):
  bonusHitDict      = {}
  bonusKeyList      = gameDataMediator.GetBonusKeyList(_gameName)
  bonusHitDict[CONST_BONUS_2X] = Get2xBonusHitCount(_gameName)
  bonusHitDict[CONST_BONUS_3X] = Get3xBonusHitCount(_gameName)
  bonusHitDict[CONST_BONUS_4X] = Get4xBonusHitCount(_gameName)
  bonusHitDict[CONST_BONUS_5X] = Get5xBonusHitCount(_gameName)
  return bonusHitDict

def GetBonusSymbolCountList(_gameName):
  reelKeysList      = gameDataMediator.GetReelKeyList(_gameName)
  reelStripsDict    = gameDataMediator.GetReelStripsDict(_gameName)
  bonusCountList    = [reelStripsDict[reelKey].count(CONST_BONUS_SYMBOL) for reelKey in reelKeysList]
  return bonusCountList

def GetReelStripLenList(_gameName):
  reelKeysList      = gameDataMediator.GetReelKeyList(_gameName)
  reelStripsDict    = gameDataMediator.GetReelStripsDict(_gameName)
  reelStripsLenList = [len(reelStripsDict[reelKey]) for reelKey in reelKeysList]
  return reelStripsLenList

def GetHitCountAtIndex(_hitIndexList, _reelLength, _gameName):
  hitCount          = 1
  bonusCountList    = GetBonusSymbolCountList(_gameName)
  reelStripsLenList = GetReelStripLenList(_gameName)
  for index in range(_reelLength):
    if index in _hitIndexList:
      hitCount *= bonusCountList[index]
    else:
      hitCount *= (reelStripsLenList[index] - bonusCountList[index])
  return hitCount

def Get2xBonusHitCount(_gameName):
  hitCount        = 0
  reelKeysList    = gameDataMediator.GetReelKeyList(_gameName)

  reelLength      = len(reelKeysList)
  indexList1      = [index for index in range(reelLength)]

  for index1 in indexList1:
    indexList2         = indexList1[index1 + 1:]
    for index2 in indexList2:
        hitIndexList   = [index1, index2]
        hitCount      += GetHitCountAtIndex(hitIndexList, reelLength, _gameName)

  return hitCount

def Get3xBonusHitCount(_gameName):
  hitCount        = 0
  reelKeysList    = gameDataMediator.GetReelKeyList(_gameName)

  reelLength      = len(reelKeysList)
  indexList1      = [index for index in range(reelLength)]

  for index1 in indexList1:
    indexList2         = indexList1[index1 + 1:]
    for index2 in indexList2:
      indexList3       = indexList1[index2 + 1:]
      for index3 in indexList3:
        hitIndexList   = [index1, index2, index3]
        hitCount      += GetHitCountAtIndex(hitIndexList, reelLength, _gameName)

  return hitCount

def Get4xBonusHitCount(_gameName):
  hitCount        = 0
  reelKeysList    = gameDataMediator.GetReelKeyList(_gameName)

  reelLength      = len(reelKeysList)
  indexList1      = [index for index in range(reelLength)]

  for index1 in indexList1:
    indexList2         = indexList1[index1 + 1:]
    for index2 in indexList2:
      indexList3       = indexList1[index2 + 1:]
      for index3 in indexList3:
        indexList4     = indexList1[index3 + 1:]
        for index4 in indexList4:
          hitIndexList = [index1, index2, index3, index4]
          hitCount    += GetHitCountAtIndex(hitIndexList, reelLength, _gameName)

  return hitCount

def Get5xBonusHitCount(_gameName):
  hitCount        = 0
  reelKeysList    = gameDataMediator.GetReelKeyList(_gameName)

  reelLength      = len(reelKeysList)
  indexList1      = [index for index in range(reelLength)]

  for index1 in indexList1:
    indexList2         = indexList1[index1 + 1:]
    for index2 in indexList2:
      indexList3       = indexList1[index2 + 1:]
      for index3 in indexList3:
        indexList4     = indexList1[index3 + 1:]
        for index4 in indexList4:
          indexList5     = indexList1[index4 + 1:]
          for index5 in indexList5:
            hitIndexList = [index1, index2, index3, index4, index5]
            hitCount    += GetHitCountAtIndex(hitIndexList, reelLength, _gameName)

  return hitCount

def GetTotalComboCounts(_gameName):
  reelLengthList    = GetReelStripLenList(_gameName)
  totalCombos       = 1
  for reelLength in reelLengthList:
    totalCombos    *= reelLength
  return totalCombos

def GetBonusHitRatioDict(_bonusHitDict, _totalComboCount, _gameName):
  bonusHitRatioDict = {}
  bonusKeyList      = gameDataMediator.GetBonusKeyList(_gameName)
  for bonuskey in bonusKeyList:
    bonusHitRatioDict[bonuskey] = float(_bonusHitDict[bonuskey]) / _totalComboCount
  return bonusHitRatioDict

def GetBonusHitRatioSum(_bonusHitRatioDict, _gameName):
  bonusKeyList      = gameDataMediator.GetBonusKeyList(_gameName)
  bonusHitRatioSum  = 0
  for bonuskey in bonusKeyList:
    bonusHitRatioSum += _bonusHitRatioDict[bonuskey]
  return bonusHitRatioSum

def GetBonusWeightedHitRatio(_bonusHitRatioDict, _gameName):
  bonusKeyList         = gameDataMediator.GetBonusKeyList(_gameName)
  bonusPayWeightDict   = gameDataMediator.GetBonusPayWeightsDict(_gameName)
  weightedBonusHitRatio = {}
  for bonuskey in bonusKeyList:
    weightedBonusHitRatio[bonuskey] = _bonusHitRatioDict[bonuskey] * bonusPayWeightDict[bonuskey]
  return weightedBonusHitRatio

def GetBonusWeightedHitSum(_bonusWeightedHitRatio, _gameName):
  bonusKeyList          = gameDataMediator.GetBonusKeyList(_gameName)
  bonusWeightedHitSum   = 0
  for bonuskey in bonusKeyList:
    bonusWeightedHitSum += _bonusWeightedHitRatio[bonuskey]
  return bonusWeightedHitSum

def main(_gameNo):
  gameName              = utility.GetGameName(_gameNo)

  maxLines              = gameDataMediator.GetMaxLines(gameName)

  bonusHitDict          = GetBonusHitDict(gameName)
  totalComboCounts      = GetTotalComboCounts(gameName)

  bonusHitRatioDict     = GetBonusHitRatioDict(bonusHitDict, totalComboCounts, gameName)
  bonusHitRatioSum      = GetBonusHitRatioSum(bonusHitRatioDict, gameName)
  bonusMaxLineHitRatio  = bonusHitRatioSum * maxLines
  bonusMaxLineFrequency = 1.0 / bonusMaxLineHitRatio

  bonusWeightedHitRatio = GetBonusWeightedHitRatio(bonusHitRatioDict, gameName)
  bonusWeightedHitSum   = GetBonusWeightedHitSum(bonusWeightedHitRatio, gameName)

  bonusPayPercentage    = gameDataMediator.GetBonusPayPercentage(gameName)
  bonusPayValue         = bonusPayPercentage / (100 * bonusWeightedHitSum)

  print 'bonusMaxLineFrequency ', bonusMaxLineFrequency
  print 'bonusPayPercentage    ', bonusPayPercentage, '%'
  print 'bonusPayValue         ', bonusPayValue, '\n'

  bonusStatsDict                          = {}
  bonusStatsDict['bonusHitDict']          = bonusHitDict
  bonusStatsDict['totalComboCounts']      = totalComboCounts
  bonusStatsDict['bonusHitRatioDict']     = bonusHitRatioDict
  bonusStatsDict['bonusHitRatioSum']      = bonusHitRatioSum
  bonusStatsDict['bonusMaxLineHitRatio']  = bonusMaxLineHitRatio
  bonusStatsDict['bonusMaxLineFrequency'] = bonusMaxLineFrequency
  bonusStatsDict['bonusWeightedHitRatio'] = bonusWeightedHitRatio
  bonusStatsDict['bonusWeightedHitSum']   = bonusWeightedHitSum
  bonusStatsDict['bonusPayPercentage']    = bonusPayPercentage
  bonusStatsDict['bonusPayValue']         = bonusPayValue

  fielStr = utility.GetFileStrForDict(bonusStatsDict)
  fileSystemManager.createBonusStatsDict(gameName, fielStr)

if __name__ == "__main__":
  main(sys.argv[1])