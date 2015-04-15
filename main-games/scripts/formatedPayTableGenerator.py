import sys
import utility
import gameDataMediator
import fileSystemManager

def GetPayTableStr(_gameName):
  symbolMapDict  = gameDataMediator.GetSymbolIDMap()
  symbolArray    = gameDataMediator.GetSymbolsArray(_gameName)
  payTableDict   = gameDataMediator.GetPayTableDict(_gameName)

  payTableStr    = '    "payTable":['
  for index in range(len(symbolArray)):
    key          = symbolArray[index]
    symbolID     = str(symbolMapDict[key])
    payTableStr += '\n'
    payTableStr += '      {\n'
    payTableStr += '        "id":' + symbolID + ',\n'
    payTableStr += '        "payout": {'
    if payTableDict[key]['5'] != 0: payTableStr +=  ' "5":' + str(payTableDict[key]['5'])
    if payTableDict[key]['4'] != 0: payTableStr += ', "4":' + str(payTableDict[key]['4'])
    if payTableDict[key]['3'] != 0: payTableStr += ', "3":' + str(payTableDict[key]['3'])
    if payTableDict[key]['2'] != 0: payTableStr += ', "2":' + str(payTableDict[key]['2'])
    payTableStr += ' }\n'
    payTableStr += '      }'
    if (index + 1 != len(symbolArray)): payTableStr += ','
    payTableStr += '\n'
  payTableStr   += '    ]'
  return payTableStr


def main(_gameNo):
  gameName = utility.GetGameName(_gameNo)
  formatedPayTableStr = GetPayTableStr(gameName)
  print formatedPayTableStr
  fileSystemManager.createFormatedPayTable(gameName, formatedPayTableStr)

if __name__ == "__main__":
  main(sys.argv[1])