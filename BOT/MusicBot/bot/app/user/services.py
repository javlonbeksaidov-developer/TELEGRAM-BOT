from app.user.models import Users
from db.database import get_db


class UserServices:
    @staticmethod
    def save_user(data: dict) -> Users:
        with get_db() as db:
            user_id = data.get("user_id")

            user = db.query(Users).filter(Users.user_id == user_id).first()

            if not user:
                user = Users(
                    user_id=user_id,
                    username=data.get("username"),
                    full_name=data.get("full_name"),
                )
                db.add(user)
            else:
                user.username = data.get("username")
                user.full_name = data.get("full_name")

            db.commit()
            db.refresh(user)
            return user

    def user_info(data: dict) -> Users:
        with get_db() as db:
            user_id = data.get("user_id")
            user = db.query(Users).filter(Users.user_id == user_id).first()

            if not user:
                return "❌ Kechirasiz, siz bazada topilmadingiz. Avval /start buyrug'ini bosing!"

            result = f"<<< {user.full_name} >>>\n1.ID: {user.user_id}\n2.Username: {user.username}"
            return result
