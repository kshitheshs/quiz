import redis
r = redis.Redis()

ANSWER_KEY = {
    "q1": "A",
    "q2": "C",
    "q3": "B"
}

def evaluate_answer(game_id, user_id, question_id, answer, timestamp):
    correct = ANSWER_KEY.get(question_id) == answer
    score = 100 if correct else 0
    r.hincrby(f"{game_id}:score", user_id, score)
    return correct, score
