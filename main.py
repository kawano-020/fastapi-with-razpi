from fastapi import FastAPI, APIRouter

from api.user import router as user_router


router = APIRouter()
router.include_router(
    user_router,
    prefix='',
    tags=['user']
)

app = FastAPI()
app.include_router(router)
