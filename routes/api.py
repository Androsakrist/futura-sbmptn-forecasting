from fastapi import APIRouter
from src.endpoints import product, user

router = APIRouter()
router.include_router(product.router)
router.include_router(user.router)

@router.get("/")
async def read_root():
    return {'message': 'Welcome to Futura: SBMPTN Forecasting app'}
