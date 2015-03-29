import sys
import json
import filePathManager

# PUBLIC FUNCTIONS
# GET FILE DATA FUNCTIONS
# INPUT FILES
def GetGeneralDataDict(_gameName):
  filePath         = filePathManager.GetGeneralDataPath(_gameName)
  generalDataDict  = _GetJSONData(filePath)
  return generalDataDict

def GetPayTableDict(_gameName):
  filePath         = filePathManager.GetPayTableFilePath(_gameName)
  payTableDict     = _GetJSONData(filePath)
  return payTableDict

def GetReelDataDict(_gameName):
  filePath         = filePathManager.GetReelDataFilePath(_gameName)
  symDistDict      = _GetJSONData(filePath)
  return symDistDict

# INTERMEDIATE FILES
def GetComboPayDict(_gameName):
  filePath         = filePathManager.GetComboPayFilePath(_gameName)
  comboPayDict     = _GetJSONData(filePath)
  return comboPayDict

def GetComboCountDict(_gameName):
  filePath         = filePathManager.GetComboCountFilePath(_gameName)
  comboCountDict   = _GetJSONData(filePath)
  return comboCountDict

def GetReelStripsDict(_gameName):
  filePath         = filePathManager.GetReelStripsFilePath(_gameName)
  reelStripsDict   = _GetJSONData(filePath)
  return reelStripsDict

# STATISTICS FILES
def GetLineStatsDict(_gameName):
  filePath         = filePathManager.GetLineStatsFilePath(_gameName)
  lineStatsDict    = _GetJSONData(filePath)
  return lineStatsDict

def GetBonusStatsDict(_gameName):
  filePath         = filePathManager.GetBonusStatsFilePath(_gameName)
  bonusStatsDict   = _GetJSONData(filePath)
  return bonusStatsDict

def GetScatterStatsDict(_gameName):
  filePath         = filePathManager.GetScatterStatsFilePath(_gameName)
  scatterStatsDict = _GetJSONData(filePath)
  return scatterStatsDict

def GetGameStatsDict(_gameName):
  filePath         = filePathManager.GetGameStatsFilePath(_gameName)
  gameStatsDict = _GetJSONData(filePath)
  return gameStatsDict

# COMMON FILES
def GetGameMapDict():
  filePath        = filePathManager.GetGameMapFilePath()
  gameMapDict     = _GetJSONData(filePath)
  return gameMapDict

def GetSymbolMapFilePath():
  filePath        = filePathManager.GetSymbolMapFilePath()
  sumbolMapDict   = _GetJSONData(filePath)
  return sumbolMapDict


# CREATE FILE FUNCTIONS
def createComboPayDict(_gameName, _comboPayDict):
  filePath    = filePathManager.GetComboPayFilePath(_gameName)
  _CreateJSONFile(filePath, _comboPayDict)

def createComboCountDict(_gameName, _comboCountDict):
  filePath    = filePathManager.GetComboCountFilePath(_gameName)
  _CreateJSONFile(filePath, _comboCountDict)

def createReelStripsDict(_gameName, _reelStripDict):
  filePath    = filePathManager.GetReelStripsFilePath(_gameName)
  _CreateJSONFile(filePath, _reelStripDict)

def createLineStatsDict(_gameName, _lineStatsDict):
  filePath    = filePathManager.GetLineStatsFilePath(_gameName)
  _CreateJSONFile(filePath, _lineStatsDict)

def createBonusStatsDict(_gameName, _bonusStatsDict):
  filePath    = filePathManager.GetBonusStatsFilePath(_gameName)
  _CreateJSONFile(filePath, _bonusStatsDict)

def createScatterStatsDict(_gameName, _scatterStatsDict):
  filePath    = filePathManager.GetScatterStatsFilePath(_gameName)
  _CreateJSONFile(filePath, _scatterStatsDict)

def createGameStatsDict(_gameName, _gameStatsDict):
  filePath    = filePathManager.GetGameStatsFilePath(_gameName)
  _CreateJSONFile(filePath, _gameStatsDict)

def createFormatedReel(_gameName, _virtualReel):
  filePath    = filePathManager.GetFormatedReelFilePath(_gameName)
  _CreateFile(filePath, _virtualReel)

def createFormatedPayTable(_gameName, _payTable):
  filePath    = filePathManager.GetFormatedPayTableFilePath(_gameName)
  _CreateFile(filePath, _payTable)

def createformatedGameData(_gameName, _gameData):
  filePath    = filePathManager.GetFormatedGameDataFilePath(_gameName)
  _CreateFile(filePath, _gameData)


# PRIVATE FUNCTIONS
def _GetFileData(_fileName):
  fileObj     = open(_fileName, 'r')
  fileStr     = fileObj.read()
  fileObj.close()
  return fileStr

def _CreateFile(_fileName, _fileStr):
  fileObj     = open(_fileName, 'w')
  fileObj.write(_fileStr)
  fileObj.close()

def _GetJSONData(_filePath):
  jsonFileObj = open(_filePath)
  jsonData    = json.load(jsonFileObj)
  jsonFileObj.close()
  return jsonData

def _CreateJSONFile(_filePath, _jsonData):
  jsonFileObj = open(_filePath, 'w')
  json.dump(_jsonData, jsonFileObj)
  jsonFileObj.close()

def main():
  print 'avaliable functions'

if __name__ == "__main__":
  main()