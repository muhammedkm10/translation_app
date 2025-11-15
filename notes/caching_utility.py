from django_redis import get_redis_connection

redis_client = get_redis_connection("default")
def increase_popularity(note_id):
    # Now safely increment score in sorted set
    redis_client.zincrby("popular_notes", 1, str(note_id))
