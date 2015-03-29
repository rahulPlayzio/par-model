import sys
import utility
import fileSystemManager
import gameDataMediator
from random import shuffle

def GenerateReelDict(_gameName):
  reelStripsDict         = {}
  reelKeyList            = gameDataMediator.GetReelKeyList(_gameName)
  symbolArray            = gameDataMediator.GetSymbolsArray(_gameName)
  symbolDistributionDict = gameDataMediator.GetSymbolDistributionDict(_gameName)

  for reelKey in reelKeyList:
    tempList = _GetPayingSymbolReel(reelKey, symbolArray, symbolDistributionDict)
    tempList = _AddSpecialSymbols(reelKey, symbolArray, symbolDistributionDict, tempList)
    reelStripsDict[reelKey] = tempList
  return reelStripsDict

def main(_gameNo):
  gameName                   = utility.GetGameName(_gameNo)
  reelStripsDict             = GenerateReelDict(gameName)
  _PrintDictData(reelStripsDict)
  fileSystemManager.createReelStripsDict(gameName, reelStripsDict)
  
def _GetPayingSymbolReel(_reelKey, _symbolArray, _symbolDistributionDict):
  tempList     = []
  for symbol in _symbolArray:
    if (utility.IsNonPaying(symbol)): continue
    tempList  += [symbol] * int(_symbolDistributionDict[symbol][_reelKey])
  shuffle(tempList)
  return tempList

def _AddSpecialSymbols(_reelKey, _symbolArray, _symbolDistributionDict, _tempList):
  counter = 0
  for symbol in _symbolArray:
    if (not utility.IsNonPaying(symbol)): continue
    for i in range(_symbolDistributionDict[symbol][_reelKey]):
      specialIndex = (counter * 3) % len(_tempList)
      _tempList.insert(specialIndex, symbol)
      counter += 1
  return _tempList

def _PrintDictData(_dictVar):
  for key in _dictVar:
    print  'length = ', len(_dictVar[key]), _dictVar[key], '\n'

if __name__ == "__main__":
  main(sys.argv[1])