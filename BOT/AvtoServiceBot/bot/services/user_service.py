from database.db import get_db


class User_Services:
    @staticmethod
    def save_user(msg):
        with get_db() as db:
            user_id = msg.user_id
            first_name = msg.first_name
            last_name = msg.last_name
            username = msg.username

            