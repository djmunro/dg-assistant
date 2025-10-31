from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.db.schema import SessionLocal
from app.models.disc import DiscCreate, DiscRead
from app.services.disc_service import DiscService

router = APIRouter()


def get_disc_service():
    return DiscService(session=SessionLocal())


@router.get("/discs", response_model=List[DiscRead])
async def get_discs(service: DiscService = Depends(get_disc_service)):
    return service.list_discs()


@router.post("/discs", response_model=DiscRead)
async def create_disc(
    disc: DiscCreate, service: DiscService = Depends(get_disc_service)
):
    return service.create_disc(disc)


@router.get("/discs/{disc_id}", response_model=DiscRead)
def get_disc(disc_id: int, service: DiscService = Depends(get_disc_service)):
    disc = service.get_disc(disc_id)
    if not disc:
        raise HTTPException(status_code=404, detail="Disc not found")
    return disc
