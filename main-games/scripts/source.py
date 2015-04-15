import sys
import utility
import reelStripGenerator
import formatedReelStripGenerator
import formatedPayTableGenerator
import bonusStatsGenerator
import scatterStatsGenerator
import scatterMultiplierStatsGenerator
import comboCountGenerator
import lineStatsGenerator
import gameStatsGenerator
import formatedGameData

def main(_gameNo):
  gameName = utility.GetGameName(_gameNo)
  reelStripGenerator.main(_gameNo)

  formatedReelStripGenerator.main(_gameNo)
  formatedPayTableGenerator.main(_gameNo)
  formatedGameData.main(_gameNo)

  bonusInGame       = bonusStatsGenerator.BonusInGame(gameName)
  scatterInGame     = scatterStatsGenerator.ScatterInGame(gameName)
  scatterMultInGame = scatterMultiplierStatsGenerator.ScatterMultInGame(gameName)

  if (bonusInGame): bonusStatsGenerator.main(_gameNo)
  if (scatterInGame): scatterStatsGenerator.main(_gameNo)
  if (scatterMultInGame): scatterMultiplierStatsGenerator.main(_gameNo)
  
  comboCountGenerator.main(_gameNo)
  lineStatsGenerator.main(_gameNo)
  gameStatsGenerator.main(_gameNo)

if __name__ == "__main__":
  main(sys.argv[1])