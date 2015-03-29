FP_INPUT_REEL_DATA      = 'input-files/reel-data.json'
FP_PAYTABLE_DATA        = 'input-files/paytable-data.json'
FP_GENERAL_GAME_DATA    = 'input-files/general-data.json'

FP_COMBO_PAY            = 'intermediate-files/combo-pay'
FP_COMBO_COUNT          = 'intermediate-files/combo-count.json'
FP_REEL_STRIP           = 'intermediate-files/reel-strips.json'

FP_LINE_STATISTICS      = 'statistics/line-pay-statistics.json'
FP_BONUS_STATISTICS     = 'statistics/bonus-statistics.json'
FP_SCATTER_STATISTICS   = 'statistics/scatter-statistics.json'
FP_GAME_STATISTICS      = 'statistics/game-statistics.json'

FP_FORMATED_REEL        = 'formated-files/virtual-reel'
FP_FORMATED_PAYTABLE    = 'formated-files/pay-table'
FP_FORMATED_GAME_DATA   = 'formated-files/game-data.json'

FP_GENERIC_TO_DEV_ID    = 'symbol-id-map.json'
FP_GAME_MAP             = 'game-map.json'
FOLDERNAME_GAME_DATA    = 'data'

# INPUT FILES
def GetGeneralDataPath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/'+ FP_GENERAL_GAME_DATA
  return filePath

# INPUT FILES
def GetPayTableFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_PAYTABLE_DATA
  return filePath

# INPUT FILES
def GetReelDataFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_INPUT_REEL_DATA
  return filePath

# INTERMEDIATE FILES
def GetComboPayFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_COMBO_PAY
  return filePath

# INTERMEDIATE FILES
def GetComboCountFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_COMBO_COUNT
  return filePath

# INTERMEDIATE FILES
def GetReelStripsFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_REEL_STRIP
  return filePath

# STATISTICS FILE
def GetLineStatsFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_LINE_STATISTICS
  return filePath

# STATISTICS FILE
def GetBonusStatsFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_BONUS_STATISTICS
  return filePath

# STATISTICS FILE
def GetScatterStatsFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_SCATTER_STATISTICS
  return filePath

# STATISTICS FILE
def GetGameStatsFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_GAME_STATISTICS
  return filePath

# DEV FILE
def GetFormatedReelFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_FORMATED_REEL
  return filePath

def GetFormatedPayTableFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_FORMATED_PAYTABLE
  return filePath

def GetFormatedGameDataFilePath(_gameName):
  filePath = _GetGameDataFolderPath(_gameName) + '/' + FP_FORMATED_GAME_DATA
  return filePath

# COMMON FILE
def GetGameMapFilePath():
  filePath = '../' + FOLDERNAME_GAME_DATA + '/' + FP_GAME_MAP
  return filePath

# COMMON FILE
def GetSymbolMapFilePath():
  filePath = '../' + FOLDERNAME_GAME_DATA + '/' + FP_GENERIC_TO_DEV_ID
  return filePath

# PRIVATE FUNCTIONS

# FOLDERNAME FOR GAME
def _GetGameDataFolderPath(_gameName):
  folderPath = '../' + FOLDERNAME_GAME_DATA + '/' + _gameName
  return folderPath

