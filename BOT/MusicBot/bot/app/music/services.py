from app.music.models import Musics
from db.database import get_db


class MusicServices:
    @staticmethod
    def save_music(data: dict) -> Musics:
        with get_db() as db:
            file_id = data.get("file_id")

            music = db.query(Musics).filter(Musics.file_id == file_id).first()

            if not music:
                music = Musics(
                    file_id=data.get("file_id"),
                    title=data.get("title"),
                    performer=data.get("performer"),
                    file_name=data.get("file_name"),
                    duration=data.get("duration"),
                    file_size=data.get("file_size"),
                )
                db.add(music)
                db.commit()

            db.refresh(music)
            return music

    @staticmethod
    def search_by_id(music_id: int) -> Musics | None:
        with get_db() as db:
            return db.query(Musics).filter(Musics.id == music_id).first()

    @staticmethod
    def search_by_title(title: str) -> list[Musics]:
        with get_db() as db:
            return db.query(Musics).filter(Musics.title.ilike(f"%{title}%")).all()
