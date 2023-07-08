import json
import sys
import threading
import time
import os
import websocket

def updateTokens():
    token = os.environ['TOKEN']
    return token

def onliner(token):
    w = websocket.WebSocket()
    w.connect('wss://gateway.discord.gg/?v=6&encoding=json')
    jsonObj = json.loads(w.recv())
    interval = jsonObj['d']['heartbeat_interval']
    w.send(json.dumps({
        "op": 2,
        "d": {
            "token": token,
            "properties": {
                "$os": sys.platform,
                "$browser": "RTB",
                "$device": f"{sys.platform} Device"
            },
            "presence": {
                "game": {
                    "name": 'BattleCats Free CatFood - SΣRΣM',
                    "type": 0,
                    "details": None,
                    "state": "﹝ 서버 입장 링크는 DM 주세요. ﹞"
                },
                "status": '>> die.ooo',
                "since": 0,
                "afk": False
            }
        },
        "s": None,
        "t": None
    }))
    while True:
        time.sleep(interval / 1000)
        w.send(json.dumps({"op": 1, "d": None}))


def main():
    oldTokens = []
    while True:
        tokens = updateTokens()
        for token in tokens:
            if not(token in oldTokens):
                print(f'Starting {token}')
                threading.Thread(target=onliner, args=(token, )).start()
                oldTokens.append(token)
        time.sleep(540)


if __name__ == '__main__':
    main()
