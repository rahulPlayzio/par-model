import sys
import utility
import fileSystemManager
import gameDataMediator

def main(_gameNo):
  gameName            =  utility.GetGameName(_gameNo)
  linePayPercentage   =  gameDataMediator.GetLinePayPercentage(gameName)
  bonusPayPercentage  =  gameDataMediator.GetBonusPayPercentage(gameName)
  scatterMultPayPer   =  gameDataMediator.GetScatterMultiPayPer(gameName)
  scatterMultiplier   =  gameDataMediator.GetScatterMultiplier(gameName)

  gamePayPercentage   =  (linePayPercentage + bonusPayPercentage + scatterMultPayPer) * scatterMultiplier
  print gamePayPercentage

  gameDataDict                    = {}
  gameDataDict['Net Payout']      = gamePayPercentage
  gameDataDict['Line Payout']     = linePayPercentage
  gameDataDict['Bonus Payout']    = bonusPayPercentage
  gameDataDict['Scatter Payout']  = scatterMultiplier
  gameDataDict['Scatter Multiplier Payout'] = scatterMultPayPer

  fileStr = utility.GetFileStrForDict(gameDataDict)
  fileSystemManager.createGameStatsDict(gameName, fileStr)

if __name__ == "__main__":
  main(sys.argv[1])