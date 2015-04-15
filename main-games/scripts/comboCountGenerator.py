import sys
import utility
import gameDataMediator
import fileSystemManager
import comboPayTableHandler

def ComboGenerator(_gameName, _comboList):
  reelStripDict     = gameDataMediator.GetReelStripsDict(_gameName)
  reelStripKey      = gameDataMediator.GetReelKeyList(_gameName)
  payBothWaysState  = gameDataMediator.GetPayBothWaysState(_gameName)
  comboCount        = [0] * len(_comboList)

  completionState   = 0
  reel1             =  reelStripDict['1']
  reel2             =  reelStripDict['2']
  reel3             =  reelStripDict['3']
  reel4             =  reelStripDict['4']
  reel5             =  reelStripDict['5']

  for index1 in range(len(reel1)):
    completionState = _PrintCompletionState(index1, reel1, completionState)
    s1 = reel1[index1]
    for s2 in reel2:
      if (utility.IsNonPaying(s1)):   break
      for s3 in reel3:
        if (utility.IsNonPaying(s2)): break
        if (_AreNonMatchingSymbols(s1, s2)):    break
        for s4 in reel4:
          for s5 in reel5:
            reelConfig        = [s1, s2, s3, s4, s5]
            reverseReelConfig = [s5, s4, s3, s2, s1]
            for index in range(len(_comboList)):
              comboPay = _comboList[index]
              strightMatchState = utility.ConfigMatches(reelConfig, comboPay)
              reverseMatchState = utility.ConfigMatches(reverseReelConfig, comboPay)
              if (strightMatchState or (payBothWaysState and reverseMatchState)):
                comboCount[index] += 1
                if (s3 == 'XWild'): comboCount[index] += 2
                break

  return comboCount

def CreateComboCountFile(_gameName):
  comboCountDict  = {}

  comboStrList    = comboPayTableHandler.GetSortedComboStrList(_gameName)
  comboList       = comboPayTableHandler.SortedComboList(_gameName)
  comboCountList  = ComboGenerator(_gameName, comboList)
  
  for index in range(len(comboStrList)):
    comboStr                 = comboStrList[index]
    comboCount               = comboCountList[index]
    comboCountDict[comboStr] = comboCount

  fielStr = utility.GetFileStrForDict(comboCountDict)
  fileSystemManager.createComboCountDict(_gameName, fielStr)


def main(_gameNo):
  gameName        = utility.GetGameName(_gameNo)
  CreateComboCountFile(gameName)

def _AreNonMatchingSymbols(_symbol1, _symbol2):
  wildList = ['Wild', 'XWild']
  return (_symbol1 != _symbol2 and _symbol1 not in wildList and _symbol2 not in wildList)

def _PrintCompletionState(_index, listVar, _completionState):
  currentCompletionState = _index * 100 / len(listVar)
  if (currentCompletionState - _completionState > 10):
    print int(currentCompletionState - 1), '% completed'
    _completionState  = currentCompletionState
  return _completionState

if __name__ == "__main__":
  main(sys.argv[1])
