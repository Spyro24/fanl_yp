import time
import random
try:
    import requests
except:
    print("some modules aren't available")

def generateGameID():
    timeStamp = int(time.time()).to_bytes(4, "big")
    randomBytes = random.getrandbits(32).to_bytes(4, "big")
    return (timeStamp + randomBytes).hex().upper()

def downloadGameFile(gameID: str, savePath: str) -> None:
    STORAGE_URL = "https://firebasestorage.googleapis.com/v0/b/fancade-live.appspot.com/o"
    downloadToken_logger = requests.get(f"{STORAGE_URL}?name=games%2F{gameID}").json()
    downloadToken = downloadToken_logger["downloadTokens"]
    game_data = requests.get(f"{STORAGE_URL}?name=games%2F{gameID}&alt=media&token={downloadToken}", stream=True)
    with open(f"{savePath}/{gameID}", "bw") as gameFile:
        for chunk in game_data.iter_content(chunk_size=64):
            gameFile.write(chunk)
        gameFile.close()
