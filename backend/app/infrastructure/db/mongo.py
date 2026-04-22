from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client["url_shortener"]

url_collection = db["urls"]


async def ensure_indexes():
    await url_collection.create_index("shortCode", unique=True)
