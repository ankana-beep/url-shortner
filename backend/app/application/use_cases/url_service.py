
import time
from app.utils.base62 import encode

class URLService:
    def __init__(self, repo, cache):
        self.repo = repo
        self.cache = cache

    async def create(self, original_url):
        unique_id = int(time.time() * 1000)
        code = encode(unique_id)

        await self.repo.save({
            "originalUrl": original_url,
            "shortCode": code
        })

        return code

    async def resolve(self, code):
        cached = await self.cache.get(code)
        if cached:
            return cached.decode()

        data = await self.repo.get(code)
        if not data:
            return None

        await self.cache.set(code, data["originalUrl"])
        await self.repo.increment(code)

        return data["originalUrl"]
