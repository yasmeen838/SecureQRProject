from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.message import Message
from models.history import History

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    total_messages = Message.query.filter_by(
        user_id=current_user.id
    ).count()

    recent_messages = Message.query.filter_by(
        user_id=current_user.id
    ).order_by(Message.created_at.desc()).limit(5).all()

    recent_history = History.query.filter_by(
        user_id=current_user.id
    ).order_by(History.scanned_at.desc()).limit(5).all()

    return render_template(
        "dashboard.html",
        user=current_user,
        total_messages=total_messages,
        recent_messages=recent_messages,
        recent_history=recent_history
    )