
from app.infrastructure.db.mongo import url_collection
from datetime import datetime

class URLRepository:
    async def save(self, data):
        data["createdAt"] = datetime.utcnow()
        data["clicks"] = 0
        await url_collection.insert_one(data)
        return data

    async def get(self, code):
        return await url_collection.find_one({"shortCode": code})

    async def increment(self, code):
        await url_collection.update_one({"shortCode": code}, {"$inc": {"clicks": 1}})
