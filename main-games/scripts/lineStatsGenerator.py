import sys
import utility
import fileSystemManager
import gameDataMediator
import comboPayTableHandler

CONST_SEPARATOR = ', '

def GetSingleLineHitCount(_gameName):
  lineHits        = 0
  comboCountDict  = gameDataMediator.GetComboCountDict(_gameName)
  comboStrList    = gameDataMediator.GetSortedComboStrList(_gameName)
  for comboStr in comboStrList:
    symbol        = comboStr.split(CONST_SEPARATOR)[0]
    comboLen      = comboStr.split(CONST_SEPARATOR)[1]
    comboPay      = comboPayTableHandler.GetValueForCombo(symbol, comboLen, _gameName)
    comboCount    = comboCountDict[comboStr]
    if (comboPay > 0):
      lineHits   += comboCount
  return lineHits

def GetTotaLineCombos(_gameName):
  lineCombos            = 1
  reelKeys              = gameDataMediator.GetReelKeyList(_gameName)
  reelStripDict         = gameDataMediator.GetReelStripsDict(_gameName)
  for reelKey in reelKeys:
    lineCombos *= len(reelStripDict[reelKey])
  return lineCombos

def GetLinePayAmount(_gameName):
  linePayAmount   = 0
  comboCountDict  = gameDataMediator.GetComboCountDict(_gameName)
  comboStrList    = gameDataMediator.GetSortedComboStrList(_gameName)
  for comboStr in comboStrList:
    symbol        = comboStr.split(CONST_SEPARATOR)[0]
    comboLen      = comboStr.split(CONST_SEPARATOR)[1]
    comboPay      = comboPayTableHandler.GetValueForCombo(symbol, comboLen, _gameName)
    comboCount    = comboCountDict[comboStr]
    if (comboPay > 0):
      linePayAmount   += int(comboCount * comboPay)
  return linePayAmount

def main(_gameNo):
  gameName              = utility.GetGameName(_gameNo)

  maxActiveLines        = gameDataMediator.GetMaxLines(gameName)

  singleLineHitCount    = GetSingleLineHitCount(gameName)
  totalLineCombos       = GetTotaLineCombos(gameName)
  linePayAmount         = GetLinePayAmount(gameName)

  singleLineHitRatio    = float(singleLineHitCount) / totalLineCombos
  linePayPercentage     = float(linePayAmount) * 100.0 / totalLineCombos
  maxLineHitRatio       = singleLineHitRatio * maxActiveLines

  print singleLineHitCount, totalLineCombos, singleLineHitRatio, linePayAmount, linePayPercentage

  lineStatsDict                        = {}
  lineStatsDict['singleLineHitCount']  = singleLineHitCount
  lineStatsDict['totalLineCombos']     = totalLineCombos
  lineStatsDict['linePayAmount']       = linePayAmount
  lineStatsDict['singleLineHitRatio']  = singleLineHitRatio
  lineStatsDict['linePayPercentage']   = linePayPercentage
  lineStatsDict['maxLineHitRatio']     = maxLineHitRatio

  fileStr = utility.GetFileStrForDict(lineStatsDict)
  fileSystemManager.createLineStatsDict(gameName, fileStr)

if __name__ == "__main__":
  main(sys.argv[1])