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
            db.refresh(movie)

            return movie
