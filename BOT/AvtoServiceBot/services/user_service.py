from database.db import get_db
from database.models import UserRoles, Users


class UserServices:
    @staticmethod
    def save_user(data: dict):
        with get_db() as db:
            user = db.query(Users).filter(Users.user_id == data["user_id"]).first()

            if not user:
                user = Users(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    user_id=data["user_id"],
                    username=data["username"],
                )
                db.add(user)
                db.commit()
                db.refresh(user)
            else:
                if (
                    user.username != data["username"]
                    or user.first_name != data["first_name"]
                    or user.last_name != data["last_name"]
                ):
                    user.username = data["username"]
                    user.first_name = data["first_name"]
                    user.last_name = data["last_name"]
                    db.commit()

            return user

    @staticmethod
    def is_user(user_id):
        with get_db() as db:
            return (
                db.query(Users)
                .filter(Users.user_id == user_id)
                .filter(Users.role == UserRoles.USER)
                .first()
            )

    @staticmethod
    def user_to_admin(user_id):
        with get_db() as db:
            user = (
                db.query(Users)
                .filter(Users.user_id == user_id, Users.role == UserRoles.USER)
                .first()
            )

            if not user:
                return None

            user.role = UserRoles.ADMIN
            db.commit()
            db.refresh(user)
            return user

    @staticmethod
    def user_count():
        with get_db() as db:
            user = db.query(Users).filter(Users.role == UserRoles.USER).all()
            return len(user)
