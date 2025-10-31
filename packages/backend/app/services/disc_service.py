from typing import List
from sqlalchemy.orm import Session

from app.db.schema import Disc
from app.models.disc import DiscCreate


class DiscService:
    def __init__(self, session: Session):
        self.db = session

    def list_discs(self) -> List[Disc]:
        return self.db.query(Disc).all()

    def create_disc(self, disc: DiscCreate) -> Disc:
        disc = Disc(name=disc.name)
        self.db.add(disc)
        self.db.commit()
        self.db.refresh(disc)
        return disc

    def get_disc(self, disc_id: int) -> Disc | None:
        return self.db.query(Disc).filter(Disc.id == disc_id).first()
