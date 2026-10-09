from javascript import require, On
import time
import math
import os
import json

mineflayer = require("mineflayer")

PLAYER_NAME = "Cthad"

watcher = mineflayer.createBot({
    "username": "watcher",
    "host": "localhost",
    "port": 25565,
    "version": "1.16.5",
})

@On(watcher, "login")
def login(this):
    print("Watcher joined!")

while True:
    time.sleep(0.1)

    player = watcher.players[PLAYER_NAME]
    if player == None:
        print(f"Could not find player")
        continue

    entity = player.entity
    if entity == None:
        os.system("cls")
        print(f"Out of render distance :(")
        continue

    os.system("cls")
    data = {
        "x": entity.position.x,
        "y": entity.position.y,
        "z": entity.position.z,
        "yaw": entity.yaw,
        "pitch": entity.pitch,
    }
    with open("minevision/player_position_data.json", "w") as f:
        json.dump(data, f)