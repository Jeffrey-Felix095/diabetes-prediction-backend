

from fastapi import APIRouter
from schemas import HealthCheck


router = APIRouter()

@router.get(
    "/health",
)
def get_health() -> HealthCheck:
    return HealthCheck(status="OK")
