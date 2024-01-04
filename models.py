from project import db, login_manager
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    uid: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(), nullable=False)
    password: Mapped[str] = mapped_column(db.String(), nullable=False)

    def get_id(self):
        return self.uid

    def verify_password(self, attempted_password):
        return self.password == attempted_password
    