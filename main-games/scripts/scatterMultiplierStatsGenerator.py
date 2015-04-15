import sys
import utility
import gameDataMediator
import fileSystemManager  
import scatterHitCalculator

CONST_SCATTER_MULTIPLIER = 'Scatter Multiplier'

def ScatterMultInGame(_gameName):
  ScatterMultInGame = utility.IsSymbolInReels(_gameName, CONST_SCATTER_MULTIPLIER)
  return ScatterMultInGame

def GetScatterMultiplierPayPercentage(_gameName):
  if (not ScatterMultInGame(_gameName)): return 0

  scatterHitDict          = scatterHitCalculator.GetScatterHitDict(_gameName, CONST_SCATTER_MULTIPLIER)
  totalCombos             = scatterHitCalculator.GetTotalComboCounts(_gameName)
  scatterHitRatioDict     = scatterHitCalculator.GetScatterHitRatio(_gameName, scatterHitDict, totalCombos)

  scatterMultiplierPayDict = gameDataMediator.GetPayValueForSymbol(_gameName, CONST_SCATTER_MULTIPLIER)
  payPercentage = 0
  for keyVar in scatterHitRatioDict:
  	payPercentage += scatterHitRatioDict[keyVar] * scatterMultiplierPayDict[keyVar]
  payPercentage *= 100
  return round(payPercentage, 4)

def main(_gameNo):
  gameName                = utility.GetGameName(_gameNo)

  scatterHitDict          = scatterHitCalculator.GetScatterHitDict(gameName, CONST_SCATTER_MULTIPLIER)
  totalCombos             = scatterHitCalculator.GetTotalComboCounts(gameName)
  scatterHitRatioDict     = scatterHitCalculator.GetScatterHitRatio(gameName, scatterHitDict, totalCombos)
  scatterHitRatioSum      = scatterHitCalculator.GetScatterHitRatioSum(gameName, scatterHitRatioDict, CONST_SCATTER_MULTIPLIER)
  scatterFrequencyDict    = scatterHitCalculator.GetScatterFrequencyDict(gameName, scatterHitRatioDict)
  scatterFrequency        = scatterHitCalculator.GetScatterFrequency(scatterHitRatioSum)

  scatterPayPercentage    = GetScatterMultiplierPayPercentage(gameName)
  print 'scatterHitRatioDict', scatterHitRatioDict
  print 'scatterFrequency', scatterFrequency
  print 'scatterPayPercentage', scatterPayPercentage

  scatterStatsStr = {}
  scatterStatsStr['scatterHitDict']       = scatterHitDict
  scatterStatsStr['totalCombos']          = totalCombos
  scatterStatsStr['scatterHitRatioDict']  = scatterHitRatioDict
  scatterStatsStr['scatterHitRatioSum']   = scatterHitRatioSum
  scatterStatsStr['scatterFrequencyDict'] = scatterFrequencyDict
  scatterStatsStr['scatterFrequency']     = scatterFrequency
  scatterStatsStr['scatterPayPercentage'] = scatterPayPercentage

  fielStr = utility.GetFileStrForDict(scatterStatsStr)
  fileSystemManager.createScatterMultiplierStatsDict(gameName, fielStr)


if __name__ == "__main__":
  main(sys.argv[1])