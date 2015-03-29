import sys
import utility
import fileSystemManager
import gameDataMediator

def GetReelStripStr(_gameName):
  reelStripDict        = gameDataMediator.GetReelStripsDict(_gameName)
  keyReelStripList     = gameDataMediator.GetReelKeyList(_gameName)
  symbolMapDict        = gameDataMediator.GetSymbolIDMap()
  reelStripStr         = '    "symbolDistribution":['
  for indexKey in range(len(keyReelStripList)):
    key    = keyReelStripList[indexKey]
    reelStripStr      += '\n      ['
    for index in range(len(reelStripDict[key])):
      item = reelStripDict[key][index]
      if (index != 0): reelStripStr += ', '
      reelStripStr += str(symbolMapDict[item])
    reelStripStr      += ']'
    if (indexKey + 1 != len(keyReelStripList)): reelStripStr += ','
  reelStripStr        += '\n]'

  return reelStripStr

def main(_gameNo):
  gameName             = utility.GetGameName(_gameNo)
  
  formatedReelStripStr = GetReelStripStr(gameName)
  print formatedReelStripStr

  fileSystemManager.createFormatedReel(gameName, formatedReelStripStr)

if __name__ == "__main__":
  main(sys.argv[1])
  