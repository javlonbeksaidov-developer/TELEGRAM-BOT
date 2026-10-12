from decouple import config

from config.db import get_db

from .models import UserRoles, Users

SUPERADMINID = config("SUPERADMINID", cast=int)


class UserServices:
    @staticmethod
    def save_user(data: dict):
        with get_db() as db:
            user = db.query(Users).filter(Users.user_id == data.get("user_id")).first()

            if not user:
                user = Users(
                    first_name=data.get("first_name"),
                    last_name=data.get("last_name"),
                    user_id=data.get("user_id"),
                    tg_username=data.get("tg_username"),
                )
                db.add(user)
                db.commit()
                db.refresh(user)

            else:
                if (
                    user.username != data.get("tg_username")
                    or user.first_name != data.get("first_name")
                    or user.last_name != data.get("last_name")
                ):
                    user.username = data.get("tg_username")
                    user.first_name = data.get("first_name")
                    user.last_name = data.get("last_name")
                    db.commit()

            return user

    @staticmethod
    def is_admin(user_id: int):
        with get_db() as db:
            admin = (
                db.query(Users)
                .filter(Users.user_id == user_id, Users.role == UserRoles.ADMIN)
                .first()
            )
            return admin

    @staticmethod
    def superadmin(user_id: int):
        return user_id == SUPERADMINID

    @staticmethod
    def full_register(data: dict):
        pass
