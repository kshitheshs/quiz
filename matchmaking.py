import uuid
import redis

r = redis.Redis()

def join_matchmaking_queue(user_id: str, subject: str):
    key = f"queue:{subject}"
    r.rpush(key, user_id)

def check_for_match(subject: str):
    key = f"queue:{subject}"
    if r.llen(key) >= 4:
        users = [r.lpop(key).decode() for _ in range(4)]
        game_id = f"game:{uuid.uuid4().hex}"
        r.hmset(game_id, {"players": ','.join(users)})
        return game_id, users
    return None, None
