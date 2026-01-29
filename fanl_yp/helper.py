import time
import random

def generateGameID():
    timeStamp = int(time.time()).to_bytes(4, "big")
    randomBytes = random.getrandbits(32).to_bytes(4, "big")
    return (timeStamp + randomBytes).hex().upper()
