from uuid import uuid4

from pymongo.errors import DuplicateKeyError

from app.utils.base62 import encode


class URLService:
    def __init__(self, repo, cache):
        self.repo = repo
        self.cache = cache

    async def create(self, original_url):
        # UUID4 is 128-bit random; base62 keeps it URL-friendly.
        for _ in range(5):
            code = encode(uuid4().int)
            try:
                await self.repo.save({
                    "originalUrl": original_url,
                    "shortCode": code,
                })
                return code
            except DuplicateKeyError:
                # Extremely unlikely; retry with a new UUID.
                continue

        raise RuntimeError("Failed to generate a unique short code")

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
