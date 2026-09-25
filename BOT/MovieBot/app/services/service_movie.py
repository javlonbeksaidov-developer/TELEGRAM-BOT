from app.db.db import get_db
from app.models.model_movie import Movies


class MovieService:
    @staticmethod
    def show_movie_by_code(code):
        with get_db() as db:
            movie = db.query(Movies).filter(Movies.code == code).first()

            if not movie:
                return None

            movie.views_count += 1
            db.commit()

            return {
                "title": movie.title,
                "code": movie.code,
                "file_id": movie.file_id,
                "views_count": movie.views_count,
            }
