from fastapi import WebSocket
import redis

r = redis.Redis()

clients = {}

async def connect_ws(websocket: WebSocket, user_id: str, game_id: str):
    await websocket.accept()
    key = f"{game_id}:{user_id}"
    clients[key] = websocket

async def send_score_update(game_id: str, message: str):
    for key, ws in clients.items():
        if key.startswith(game_id):
            await ws.send_text(message)
