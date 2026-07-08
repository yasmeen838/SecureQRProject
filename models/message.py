from database import db
from datetime import datetime


class Message(db.Model):
    __tablename__ = "messages"

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # User who generated the QR
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    # Encrypted Message
    encrypted_message = db.Column(
        db.Text,
        nullable=False
    )

    # Secret Key (for now stored as plain text;
    # later we can change this to a hashed value)
    secret_key = db.Column(
        db.String(255),
        nullable=False
    )

    # Generated QR Image Path
    qr_image = db.Column(
        db.String(255),
        nullable=True
    )

    # Date & Time
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Relationship with User table
    user = db.relationship(
        "User",
        backref=db.backref("messages", lazy=True)
    )

    def __repr__(self):
        return f"<Message {self.id}>"