import sys
import reelStripGenerator
import formatedReelStripGenerator
import formatedPayTableGenerator
import bonusStatsGenerator
import scatterStatsGenerator
import comboCountGenerator
import lineStatsGenerator
import gameStatsGenerator
import formatedGameData

def main(_gameNo):
  reelStripGenerator.main(_gameNo)

  formatedReelStripGenerator.main(_gameNo)
  formatedPayTableGenerator.main(_gameNo)
  formatedGameData.main(_gameNo)

  bonusStatsGenerator.main(_gameNo)
  scatterStatsGenerator.main(_gameNo)
  
  comboCountGenerator.main(_gameNo)
  lineStatsGenerator.main(_gameNo)
  gameStatsGenerator.main(_gameNo)

if __name__ == "__main__":
  main(sys.argv[1])