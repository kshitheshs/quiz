import redis
r = redis.Redis()

def update_leaderboard(user_id, score, country="IN"):
    r.zincrby("leaderboard:global", score, user_id)
    r.zincrby(f"leaderboard:{country}", score, user_id)

def get_leaderboard(global_lb=True, country="IN", top_n=10):
    key = "leaderboard:global" if global_lb else f"leaderboard:{country}"
    return r.zrevrange(key, 0, top_n - 1, withscores=True)
