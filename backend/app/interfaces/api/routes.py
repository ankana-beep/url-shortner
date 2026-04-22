
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from app.config.settings import settings
from app.application.use_cases.url_service import URLService
from app.infrastructure.repositories.url_repo import URLRepository
from app.infrastructure.cache.redis_cache import RedisCache

router = APIRouter()

def get_service():
    return URLService(URLRepository(), RedisCache())

@router.post("/shorten")
async def shorten(req: dict, service: URLService = Depends(get_service)):
    code = await service.create(req["url"])
    return {"shortUrl": f"{settings.BASE_URL}/{code}"}

@router.get("/{code}")
async def redirect(code: str, service: URLService = Depends(get_service)):
    url = await service.resolve(code)
    if not url:
        return {"error": "Not found"}
    return RedirectResponse(url)
