from django.core.cache import cache

def increase_popularity(note_id):
    redis_client = cache.client.get_client()
    redis_client.zincrby("popular_notes", 1, note_id)