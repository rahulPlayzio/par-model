import sys
import utility
import gameDataMediator
import fileSystemManager
import formatedPayTableGenerator
import formatedReelStripGenerator

def main(_gameNo):
  gameName    = utility.GetGameName(_gameNo)

  gameDataStr = ''
  version     = gameDataMediator.GetVersion(gameName)
  gameId      = gameDataMediator.GetGameId(gameName)
  name        = gameDataMediator.GetName(gameName)
  reelsCount  = gameDataMediator.GetReelCount(gameName)
  rowsCount   = gameDataMediator.GetRowCount(gameName)
  maxLines    = gameDataMediator.GetMaxLines(gameName)
  
  formatedReelStripStr = formatedReelStripGenerator.GetReelStripStr(gameName)
  formatedPayTableStr  = formatedPayTableGenerator.GetPayTableStr(gameName)

  gameDataStr  += '{\n'
  gameDataStr  += '    "version":    "' + str(version)    + '",\n'
  gameDataStr  += '    "gameId":      ' + str(gameId)     + ',\n'
  gameDataStr  += '    "name":       "' + str(name)       + '",\n'
  gameDataStr  += '    "reelsCount":  ' + str(reelsCount) + ',\n'
  gameDataStr  += '    "rowsCount":   ' + str(rowsCount)  + ',\n'
  gameDataStr  += '    "maxLines":    ' + str(maxLines)   + ',\n'

  gameDataStr  += formatedReelStripStr
  gameDataStr  += ",\n"
  gameDataStr  += formatedPayTableStr
  gameDataStr  += "\n}"

  fileSystemManager.createformatedGameData(gameName, gameDataStr)

if __name__ == "__main__":
  main(sys.argv[1])