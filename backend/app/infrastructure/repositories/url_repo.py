
from app.infrastructure.db.mongo import url_collection
from datetime import datetime

class URLRepository:
    async def save(self, data):
        data["created_at"] = datetime.utcnow()
        data["clicks"] = 0
        await url_collection.insert_one(data)
        return data

    async def get(self, code):
        return await url_collection.find_one({"short_code": code})

    async def increment(self, code):
        await url_collection.update_one({"short_code": code}, {"$inc": {"clicks": 1}})
