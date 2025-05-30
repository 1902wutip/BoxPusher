import numpy as np


##  ================= Map Definition =================
##  map encode
EMPTY = 0
WALL = 1
TARGET = 2
BOX = 3
PLAYER = 4
maps = []    ##  every element in maps in a map


##  ================= Level 1 =================
##  limiting requirement
TIME_LIMIT = 20
MOVE_LIMIT = 5

##  initial map
game_map = np.array([
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
])

##  insert map to maps
maps.append({"TIME_LIMIT":TIME_LIMIT,
             "MOVE_LIMIT":MOVE_LIMIT,
             "game_map":game_map})


##  ================= Level 2 =================
##  limiting requirement
TIME_LIMIT = 60
MOVE_LIMIT = 100

##  initial map
game_map = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 3, 1, 3, 1, 3, 1, 3, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

##  insert map to maps
maps.append({"TIME_LIMIT":TIME_LIMIT,
             "MOVE_LIMIT":MOVE_LIMIT,
             "game_map":game_map})


##  ================= Level 3 =================
##  limiting requirement
TIME_LIMIT = 60
MOVE_LIMIT = 120

##  initial map
game_map = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 1, 0, 1, 3, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 4, 1, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 2, 2, 2, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

##  insert map to maps
maps.append({"TIME_LIMIT":TIME_LIMIT,
             "MOVE_LIMIT":MOVE_LIMIT,
             "game_map":game_map})


##  ================= Level 4 =================
##  limiting requirement
TIME_LIMIT = 60
MOVE_LIMIT = 80

##  initial map
game_map = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 3, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 2, 1, 0, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 3, 0, 2, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

##  insert map to maps
maps.append({"TIME_LIMIT":TIME_LIMIT,
             "MOVE_LIMIT":MOVE_LIMIT,
             "game_map":game_map})


##  ================= Level 5 =================
##  limiting requirement
TIME_LIMIT = 90
MOVE_LIMIT = 125

##  initial map
game_map = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 2, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 2, 1, 3, 0, 1],
    [1, 0, 1, 0, 1, 2, 1, 0, 0, 1],
    [1, 0, 3, 0, 1, 2, 1, 3, 1, 1],
    [1, 0, 0, 0, 1, 2, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

##  insert map to maps
maps.append({"TIME_LIMIT":TIME_LIMIT,
             "MOVE_LIMIT":MOVE_LIMIT,
             "game_map":game_map})


##  ================= Level 6 =================
##  limiting requirement
TIME_LIMIT = 120
MOVE_LIMIT = 300

##  initial map
game_map = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 4, 0, 0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 3, 0, 1, 2, 2, 1],
    [1, 0, 0, 0, 1, 0, 3, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

##  insert map to maps
maps.append({"TIME_LIMIT":TIME_LIMIT,
             "MOVE_LIMIT":MOVE_LIMIT,
             "game_map":game_map})


##  ================= Level 7 =================
##  limiting requirement
TIME_LIMIT = 120
MOVE_LIMIT = 400

##  initial map
game_map = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 3, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 3, 0, 3, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 3, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 4, 1, 1, 1, 1, 1, 1, 0, 3, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

##  insert map to maps
maps.append({"TIME_LIMIT":TIME_LIMIT,
             "MOVE_LIMIT":MOVE_LIMIT,
             "game_map":game_map})


##  ================= Level 8 =================
##  limiting requirement
TIME_LIMIT = 150
MOVE_LIMIT = 200

##  initial map
game_map = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 2, 0, 0, 1, 0, 0, 3, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 3, 0, 3, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

##  insert map to maps
maps.append({"TIME_LIMIT":TIME_LIMIT,
             "MOVE_LIMIT":MOVE_LIMIT,
             "game_map":game_map})


##  ================= Level 9 =================
##  limiting requirement
TIME_LIMIT = 60
MOVE_LIMIT = 90

#  initial map
game_map = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 2, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 4, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 2, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

##  insert map to maps
maps.append({"TIME_LIMIT":TIME_LIMIT,
             "MOVE_LIMIT":MOVE_LIMIT,
             "game_map":game_map})


##  ================= Level 10 =================
##  limiting requirement
TIME_LIMIT = 120
MOVE_LIMIT = 150

game_map = np.array([
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 4, 0, 0, 0, 2, 0, 0, 3, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 3, 0, 0, 2, 0, 0, 0, 2, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0]
])

##  insert map to maps
maps.append({"TIME_LIMIT":TIME_LIMIT,
             "MOVE_LIMIT":MOVE_LIMIT,
             "game_map":game_map})