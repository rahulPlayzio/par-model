import utility
import fileSystemManager
from comboPayTableHandler import GetSortedComboStrList

# INPUT FILES
# GENERAL GAME DATA FILES
def GetMaxLines(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  maxLines               = generalGameDataDict['maxLines']
  return maxLines

def GetBonusPayPercentage(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  bonusPayPercentage     = generalGameDataDict['bonusPayPercentage']
  return bonusPayPercentage

def GetSymbolsArray(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  symbolArray            = generalGameDataDict['symbols']
  return symbolArray

def GetBonusKeyList(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  bonusKeyList           = generalGameDataDict['bonuskeys']
  return bonusKeyList

def GetScatterKeyList(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  scatterKeyList         = generalGameDataDict['scatterKeys']
  return scatterKeyList

def GetBonusPayWeightsDict(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  bonusPayWeightsDict    = generalGameDataDict['bonusPayWeights']
  return bonusPayWeightsDict

def GetScatterFreeSpinDict(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  scatterFreeSpinDict    = generalGameDataDict['scatterFreeSpins']
  return scatterFreeSpinDict

def GetBonusPayPercentage(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  bonusPayPercentage     = generalGameDataDict['bonusPayPercentage']
  return bonusPayPercentage

def GetVersion(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  gameVersion            = generalGameDataDict['version']
  return gameVersion

def GetGameId(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  gameId                 = generalGameDataDict['gameId']
  return gameId

def GetName(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  name                   = generalGameDataDict['name']
  return name

def GetReelCount(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  reelsCount             = generalGameDataDict['reelsCount']
  return reelsCount

def GetRowCount(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  rowsCount              = generalGameDataDict['rowsCount']
  return rowsCount

def GetPayBothWaysState(_gameName):
  generalGameDataDict    = fileSystemManager.GetGeneralDataDict(_gameName)
  payBothWaysState       = generalGameDataDict['payBothWays']
  if (payBothWaysState is None): return False
  return payBothWaysState

# PAYTABLE FILES
def GetPayTableDict(_gameName):
  payTableDict           = fileSystemManager.GetPayTableDict(_gameName)
  return payTableDict

# REEL DATA FILES
def GetSymbolDistributionDict(_gameName):
  reelDataDicts          = fileSystemManager.GetReelDataDict(_gameName)
  symbolDistributionDict = reelDataDicts['symbolDistribution']
  return symbolDistributionDict

def GetReelKeyList(_gameName):
  reelDataDicts          = fileSystemManager.GetReelDataDict(_gameName)
  reelKeyList            = reelDataDicts['reelKeys']
  return reelKeyList
  
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
  scatterStatsDict       = fileSystemManager.GetScatterStatsDict(_gameName)
  scatterMultiplier      = scatterStatsDict['scatterMultiplier']
  return scatterMultiplier

# COMMON FILES
def GetGameMapDict():
  gameMapDict            = fileSystemManager.GetGameMapDict()
  return gameMapDict

def GetSymbolIDMap():
  symbolMapDict          = fileSystemManager.GetSymbolMapFilePath()
  return symbolMapDict

# FROM OTHER SCRIPTS
'''
def GetComboCountList():
  comboCountDict      = GetComboCountDict(_gameName)
  comboStrList        = GetSortedComboStrList(_gameName)
  comboCountList      = [comboCountDict[keyVar] for keyVar in comboStrList]
  return comboCountList
'''
if __name__ == "__main__":
  print GetMaxLines('machine 1 - farm')
