import sys
import const
import utility
import gameDataMediator

def GetValueForCombo(_symbol, _comboLenStr, _gameName):
  payTableDict = gameDataMediator.GetPayTableDict(_gameName)
  return int(payTableDict[_symbol][_comboLenStr])

def GenerateSortedComboPayDict(_gameName):
  comboPayDict = {}
  symbolList   = gameDataMediator.GetSymbolsArray(_gameName)
  payTableDict = gameDataMediator.GetPayTableDict(_gameName)

  for symbol in symbolList:
    if (symbol == 'Scatter' or symbol == 'Bonus'): continue
    for index in range(4):
      comboLen = index + 2
      key      = symbol + const.COMBO_LENGTH_SEPARATOR + str(comboLen)
      value    = payTableDict[symbol][str(comboLen)]
      comboPayDict[key] = value

  sortedComboPayList = utility.GetSortedDictByValue(comboPayDict)
  return sortedComboPayList

def GetSortedComboStrList(_gameName):
  sortedComboPayList = GenerateSortedComboPayDict(_gameName)
  sortedComboStrList = [x[0] for x in sortedComboPayList]
  return sortedComboStrList

def GetSortedPayList(_gameName):
  sortedComboPayList = GenerateSortedComboPayDict(_gameName)
  sortedComboStrList = [int(x[1]) for x in sortedComboPayList]
  return sortedComboStrList

def SortedComboList(_gameName):
  sortedComboStrList = GetSortedComboStrList(_gameName)
  sortedComboList    = []
  for comboPay in sortedComboStrList:
    symbol           = comboPay.split(const.COMBO_LENGTH_SEPARATOR)[0]
    comboLen         = int(comboPay.split(const.COMBO_LENGTH_SEPARATOR)[1])
    sortedComboList.append([symbol] * comboLen)
  return sortedComboList

def main(_gameNo):
  gameName           = utility.GetGameName(_gameNo)
  sortedComboList    = GetSortedComboPayList(gameName)
  print sortedComboList

if __name__ == "__main__":
  main(sys.argv[1])