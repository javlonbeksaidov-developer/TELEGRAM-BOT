from database.db import get_db
from database.models import UserRoles, Users


class AdminServices:
    @staticmethod
    def is_admin(user_id):
        with get_db() as db:
            return (
                db.query(Users)
                .filter(Users.user_id == user_id)
                .filter(Users.role == UserRoles.ADMIN)
                .first()
            )

    @staticmethod
    def admin_to_user(user_id):
        with get_db() as db:
            admin = (
                db.query(Users)
                .filter(Users.user_id == user_id, Users.role == UserRoles.ADMIN)
                .first()
            )

            if not admin:
                return None

            admin.role = UserRoles.USER
            db.commit()
            db.refresh(admin)
            return admin

    @staticmethod
    def admin_count():
        with get_db() as db:
            admin = db.query(Users).filter(Users.role == UserRoles.ADMIN).all()
            return len(admin)
