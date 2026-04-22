
import redis.asyncio as redis
from app.config.settings import settings

client = redis.from_url(settings.REDIS_URI)

class RedisCache:
    async def get(self, key):
        return await client.get(key)

    async def set(self, key, value):
        await client.set(key, value, ex=3600)
