import random

from app.db.db import get_db
from app.models.model_movie import Movies


class MovieService:
    @staticmethod
    def code_gen_id():
        with get_db() as db:
            while True:
                code = random.randint(1000, 9999)
                db_code = db.query(Movies).filter(Movies.code == code).first()
                if not db_code:
                    return code

    @staticmethod
    def save_movie(data: dict):
        with get_db() as db:
            movie = db.query(Movies).filter(Movies.file_id == data["file_id"]).first()

            if not movie:
                movie = Movies(
                    code=data["code"],
                    title=data["title"],
                    description=data["description"],
                    file_id=data["file_id"],
                    duration=data["duration"],
                    file_size=data["file_size"],
                    views_count=data["views_count"],
                )
                db.add(movie)
                db.commit()
                db.refresh(movie)
            else:
                if (
                    movie.code != data["code"]
                    or movie.title != data["title"]
                    or movie.description != data["description"]
                ):
                    movie.code = data["code"]
                    movie.title = data["title"]
                    movie.description = data["description"]
                    db.commit()
                    db.refresh(movie)

            return movie

    @staticmethod
    def show_movie_all_db():
        with get_db() as db:
            return db.query(Movies).all()

    @staticmethod
    def show_movie_by_id_db(code):
        with get_db() as db:
            return db.query(Movies).filter(Movies.code == code).first()

    @staticmethod
    def statistic_movie_count():
        with get_db() as db:
            movies = db.query(Movies).all()
            return len(movies)
