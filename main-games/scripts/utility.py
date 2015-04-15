import copy
import operator
import gameDataMediator

def GetGameName(_gameNo):
  gameMapDict      = gameDataMediator.GetGameMapDict()
  gameName         = gameMapDict[_gameNo]
  return gameName

def IsNonPaying(_symbol):
  if (_symbol == 'Scatter' or _symbol == 'Bonus' or _symbol == 'Scatter Multiplier' or _symbol == 'XWild'): return True
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

def RemoveKeyFromDict(_dict, _key):
  newDict = dict(_dict)
  del newDict[_key]
  return newDict

def RemoveItemFromList(_list, _item):
  newList = copy.copy(_list)
  newList.remove(_item)
  return newList

def IsSymbolInReels(_gameName, _symbol):
  symbolArray = gameDataMediator.GetSymbolsArray(_gameName)
  return (_symbol in symbolArray)

def isNumber(_item):
  try:
    float(_item)
    return True
  except ValueError:
    return False

def GetFileStrForDict(_dictVar, _length = 1):
  strVar = ''
  strVar = '{\n'
  firstIteration = True
  for keyVar in _dictVar:
    value   = _dictVar[keyVar]
    if type(value) == type({}): value = GetFileStrForDict(value, _length + 1)
    #else:                       value = round(value, 7)
    
    if (firstIteration):
      strVar += '\n'
      firstIteration = False
    else:
      strVar += ',\n'

    strVar += ('\t' * _length)
    strVar += '\"'   + str(keyVar) + '\"'
    strVar += ': '
    strVar += str(value)

  strVar += ('\n\t' * _length)
  strVar += '}'
  return strVar

