from app.db.db import get_db
from app.models.model_user import Users


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
