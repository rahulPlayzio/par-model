import utility
import fileSystemManager
import scatterMultiplierStatsGenerator
from comboPayTableHandler import GetSortedComboStrList

# INPUT FILES
# GENERAL GAME DATA FILES
def GetMaxLines(_gameName):
  generalGameDataDict    = fileSystemManager.GetMainGameDataDict(_gameName)
  maxLines               = generalGameDataDict['maxLines']
  return maxLines

def GetBonusPayPercentage(_gameName):
  generalGameDataDict    = fileSystemManager.GetMainGameDataDict(_gameName)
  bonusPayPercentage     = generalGameDataDict['bonusPayPercentage']
  return bonusPayPercentage

def GetSymbolsArray(_gameName):
  symbolDistributionDict = GetSymbolDistributionDict(_gameName)
  symbolArray            = symbolDistributionDict.keys()
  return symbolArray

def GetBonusKeyList(_gameName):
  bonusPayWeightsDict    = GetBonusPayWeightsDict(_gameName)
  bonusKeyList           = bonusPayWeightsDict.keys()
  return bonusKeyList

def GetScatterKeyList(_gameName):
  scatterFreeSpinDict    = GetScatterFreeSpinDict(_gameName)
  scatterKeyList         = scatterFreeSpinDict.keys()
  return scatterKeyList

def GetBonusPayWeightsDict(_gameName):
  payTableDict           = GetPayTableDict(_gameName)
  bonusPayWeightsDict    = payTableDict['Bonus']
  return bonusPayWeightsDict

def GetScatterFreeSpinDict(_gameName):
  payTableDict           = GetPayTableDict(_gameName)
  scatterFreeSpinDict    = payTableDict['Scatter']
  return scatterFreeSpinDict

def GetBonusPayPercentage(_gameName):
  generalGameDataDict    = fileSystemManager.GetMainGameDataDict(_gameName)
  bonusPayPercentage     = 0
  if ('bonusPayPercentage' in generalGameDataDict.keys()):
    bonusPayPercentage     = generalGameDataDict['bonusPayPercentage']
  return bonusPayPercentage

def GetVersion(_gameName):
  generalGameDataDict    = fileSystemManager.GetMainGameDataDict(_gameName)
  gameVersion            = generalGameDataDict['version']
  return gameVersion

def GetGameId(_gameName):
  generalGameDataDict    = fileSystemManager.GetMainGameDataDict(_gameName)
  gameId                 = generalGameDataDict['gameId']
  return gameId

def GetName(_gameName):
  generalGameDataDict    = fileSystemManager.GetMainGameDataDict(_gameName)
  name                   = generalGameDataDict['name']
  return name

def GetReelCount(_gameName):
  generalGameDataDict    = fileSystemManager.GetMainGameDataDict(_gameName)
  reelsCount             = generalGameDataDict['reelsCount']
  return reelsCount

def GetRowCount(_gameName):
  generalGameDataDict    = fileSystemManager.GetMainGameDataDict(_gameName)
  rowsCount              = generalGameDataDict['rowsCount']
  return rowsCount

def GetPayBothWaysState(_gameName):
  generalGameDataDict    = fileSystemManager.GetMainGameDataDict(_gameName)
  payBothWaysState       = generalGameDataDict['payBothWays']
  if (payBothWaysState is None): return False
  return payBothWaysState

# PAYTABLE FILES
def GetPayTableDict(_gameName):
  fileDataDict           = fileSystemManager.GetMainGameDataDict(_gameName)
  payTableDict           = fileDataDict['payTable']
  return payTableDict

def GetPayValueForSymbol(_gameName, _symbol):
  fileDataDict           = fileSystemManager.GetMainGameDataDict(_gameName)
  payTableDict           = fileDataDict['payTable']
  symbolPayDict          = payTableDict[_symbol]
  return symbolPayDict

# REEL DATA FILES
def GetSymbolDistributionDict(_gameName):
  fileDataDict           = fileSystemManager.GetMainGameDataDict(_gameName)
  symbolDistributionDict = fileDataDict['symbolDistribution']
  return symbolDistributionDict

def GetReelKeyList(_gameName):
  symbolDistributionDict = GetSymbolDistributionDict(_gameName)
  reelKeyList            = symbolDistributionDict['HP1'].keys()
  return reelKeyList
  
def GetSymbolCountList(_gameName, _symbol):
  symbolDistributionDict = GetSymbolDistributionDict(_gameName)
  symbolDict             = symbolDistributionDict[_symbol]
  return symbolDict

# INTERMEDIATE FILES
def GetComboPayDict(_gameName):
  comboPayDict         = fileSystemManager.GetComboPayDict(_gameName)
  return comboCountDict

def GetComboCountDict(_gameName):
  comboCountDict         = fileSystemManager.GetComboCountDict(_gameName)
  return comboCountDict

def GetReelStripsDict(_gameName):
  reelStripDict          = fileSystemManager.GetReelStripsDict(_gameName)
  return reelStripDict

# STATISTICS FILES
def GetLinePayPercentage(_gameName):
  lineStatsDict          = fileSystemManager.GetLineStatsDict(_gameName)
  linePayPercentage      = lineStatsDict['linePayPercentage']
  return linePayPercentage

def GetScatterMultiplier(_gameName):
  scatterStatsDict        = fileSystemManager.GetScatterStatsDict(_gameName)
  scatterMultiplierFactor = scatterStatsDict['scatterMultiplierFactor']
  return scatterMultiplierFactor

def GetScatterMultiPayPer(_gameName):
  scatterMultiPayPer      = scatterMultiplierStatsGenerator.GetScatterMultiplierPayPercentage(_gameName)
  return scatterMultiPayPer

# COMMON FILES
def GetGameMapDict():
  gameMapDict            = fileSystemManager.GetGameMapDict()
  return gameMapDict

def GetSymbolIDMap():
  symbolMapDict          = fileSystemManager.GetSymbolMapFilePath()
  return symbolMapDict

# FROM OTHER SCRIPTS
if __name__ == "__main__":
  print GetMaxLines('machine 1 - farm')
