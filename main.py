from fastapi import FastAPI, WebSocket
from models import User, AnswerSubmission
from matchmaking import join_matchmaking_queue, check_for_match
from scoring import evaluate_answer
from leaderboard import update_leaderboard, get_leaderboard
from websocket import connect_ws, send_score_update

app = FastAPI()

@app.post("/matchmaking/join")
def join(user: User):
    join_matchmaking_queue(user.user_id, user.subject)
    game_id, users = check_for_match(user.subject)
    if game_id:
        return {"status": "matched", "game_id": game_id, "users": users}
    return {"status": "queued"}

@app.post("/scoring/submit")
def score(submission: AnswerSubmission):
    correct, points = evaluate_answer(submission.game_id, submission.user_id,
                                      submission.question_id, submission.answer,
                                      submission.timestamp)
    update_leaderboard(submission.user_id, points)
    return {"correct": correct, "score": points}

@app.get("/leaderboard/global")
def get_global():
    return get_leaderboard()

@app.websocket("/ws/{user_id}/{game_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str, game_id: str):
    await connect_ws(websocket, user_id, game_id)
    while True:
        data = await websocket.receive_text()
        await send_score_update(game_id, f"{user_id} says: {data}")
