import sys
import utility
import fileSystemManager
import gameDataMediator

def main(_gameNo):
  gameName            =  utility.GetGameName(_gameNo)
  linePayPercentage   =  gameDataMediator.GetLinePayPercentage(gameName)
  bonusPayPercentage  =  gameDataMediator.GetBonusPayPercentage(gameName)
  scatterMultiplier   =  gameDataMediator.GetScatterMultiplier(gameName)

  gamePayPercentage   =  (linePayPercentage + bonusPayPercentage) * scatterMultiplier
  print gamePayPercentage

  gameDataDict                    = {}
  gameDataDict['Net Payout']      = gamePayPercentage
  gameDataDict['Line Payout']     = linePayPercentage
  gameDataDict['Bonus Payout']    = bonusPayPercentage
  gameDataDict['Scatter Payout']  = scatterMultiplier

  fileSystemManager.createGameStatsDict(gameName, gameDataDict)

if __name__ == "__main__":
  main(sys.argv[1])