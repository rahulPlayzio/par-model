import operator
import gameDataMediator

def GetGameName(_gameNo):
  gameMapDict      = gameDataMediator.GetGameMapDict()
  gameName         = gameMapDict[_gameNo]
  return gameName

def IsNonPaying(_symbol):
  if (_symbol == 'Scatter' or _symbol == 'Bonus'): return True
  else: return False

def GetSortedDictByValue(_dictVar):
  _sortedDict = sorted(_dictVar.items(), key = operator.itemgetter(1), reverse = True)
  return _sortedDict

def ConfigMatches(_reelConfigList, _comboPayList):
  comboLen = len(_comboPayList)
  for i in range(comboLen):
    if (_reelConfigList[i] != _comboPayList[i] and _reelConfigList[i] != 'Wild'):
      return False
  return True

'''
def ExchangeStrAtIndex(_strList, _index1, _index2):
  temp               = _strList[_index1]
  _strList[_index1]  = _strList[_index2]
  _strList[_index2]  = temp
  return _strList

def GetBonusPayPercentage(_gameName):
  filePathBonusPay =  fileNameManager.getBonusPayFilePath(_gameName)
  bonusPay         =  getFileData(filePathBonusPay)
  return bonusPay

def GetDictFromList(_valueList, _keyList):
  listLength = len(_valueList)
  dictVar    = {}
  for index in range(listLength):
    dictVar[_keyList[index]] = _valueList[index]
  return dictVar

'''