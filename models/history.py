from datetime import datetime
from database import db


class History(db.Model):
    __tablename__ = "history"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    message_id = db.Column(
        db.Integer,
        db.ForeignKey("messages.id"),
        nullable=False
    )

    action = db.Column(
        db.String(50),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="Success"
    )

    scanned_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Relationships
    user = db.relationship(
        "User",
        backref=db.backref("history", lazy=True)
    )

    message = db.relationship(
        "Message",
        backref=db.backref("history", lazy=True)
    )

    def __repr__(self):
        return f"<History {self.id}>"