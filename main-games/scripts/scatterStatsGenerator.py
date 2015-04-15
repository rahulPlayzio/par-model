import sys
import utility
import fileSystemManager
import gameDataMediator
import scatterHitCalculator

CONST_REEL_ROWS      = 3
CONST_SCATTER_SYMBOL = 'Scatter'

def ScatterInGame(_gameName):
  scatterInGame = utility.IsSymbolInReels(_gameName, CONST_SCATTER_SYMBOL)
  return scatterInGame

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
  scatterHitDict        = scatterHitCalculator.GetScatterHitDict(_gameName, CONST_SCATTER_SYMBOL)
  totalCombos           = scatterHitCalculator.GetTotalComboCounts(_gameName)
  scatterHitRatioDict   = scatterHitCalculator.GetScatterHitRatio(_gameName, scatterHitDict, totalCombos)
  scatterPayFactorDict  = GetScatterPayFactorDict(_gameName, scatterHitRatioDict)
  scatterPayFactorSum   = GetPayFactorSum(_gameName, scatterPayFactorDict)
  scatterMultiplier     = 1.0 / (1- scatterPayFactorSum)
  return scatterMultiplier

def main(_gameNo):
  gameName                = utility.GetGameName(_gameNo)

  scatterHitDict          = scatterHitCalculator.GetScatterHitDict(gameName, CONST_SCATTER_SYMBOL)
  totalCombos             = scatterHitCalculator.GetTotalComboCounts(gameName)
  scatterHitRatioDict     = scatterHitCalculator.GetScatterHitRatio(gameName, scatterHitDict, totalCombos)
  scatterHitRatioSum      = scatterHitCalculator.GetScatterHitRatioSum(gameName, scatterHitRatioDict, CONST_SCATTER_SYMBOL)
  scatterFrequencyDict    = scatterHitCalculator.GetScatterFrequencyDict(gameName, scatterHitRatioDict)
  scatterFrequency        = scatterHitCalculator.GetScatterFrequency(scatterHitRatioSum)

  scatterPayFactorDict    = GetScatterPayFactorDict(gameName, scatterHitRatioDict)
  scatterPayFactorSum     = GetPayFactorSum(gameName, scatterPayFactorDict)
  scatterMultiplierFactor = GenerateScatterMultiplier(gameName)

  scatterStatsStr                            = {}
  scatterStatsStr['scatterHitDict']          = scatterHitDict
  scatterStatsStr['totalCombos']             = totalCombos
  scatterStatsStr['scatterHitRatioDict']     = scatterHitRatioDict
  scatterStatsStr['scatterHitRatioSum']      = scatterHitRatioSum
  scatterStatsStr['scatterFrequencyDict']    = scatterFrequencyDict
  scatterStatsStr['scatterFrequency']        = scatterFrequency
  scatterStatsStr['scatterPayFactorDict']    = scatterPayFactorDict
  scatterStatsStr['scatterPayFactorSum']     = scatterPayFactorSum
  scatterStatsStr['scatterMultiplierFactor'] = scatterMultiplierFactor

  print 'scatterFrequency        ', scatterFrequency
  print 'scatterMultiplierFactor ', scatterMultiplierFactor, '\n'

  fielStr = utility.GetFileStrForDict(scatterStatsStr)
  fileSystemManager.createScatterStatsDict(gameName, fielStr)

if __name__ == "__main__":
  main(sys.argv[1])