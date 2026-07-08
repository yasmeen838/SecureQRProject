from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from database import db
from models.user import User
from models.message import Message
from models.history import History

admin_bp = Blueprint("admin", __name__)


def admin_required():
    """
    Check whether the logged-in user is an administrator.
    """
    return current_user.is_authenticated and current_user.role == "admin"


# ----------------------------------------
# Admin Dashboard
# ----------------------------------------
@admin_bp.route("/admin")
@login_required
def admin_dashboard():

    if not admin_required():
        flash("Access denied.", "danger")
        return redirect(url_for("dashboard.dashboard"))

    users = User.query.order_by(User.created_at.desc()).all()

    messages = Message.query.order_by(
        Message.created_at.desc()
    ).all()

    history = History.query.order_by(
        History.scanned_at.desc()
    ).all()

    return render_template(
        "admin.html",
        users=users,
        messages=messages,
        history=history,
        total_users=len(users),
        total_messages=len(messages),
        total_history=len(history)
    )


# ----------------------------------------
# Delete User
# ----------------------------------------
@admin_bp.route("/admin/delete-user/<int:user_id>")
@login_required
def delete_user(user_id):

    if not admin_required():
        flash("Access denied.", "danger")
        return redirect(url_for("dashboard.dashboard"))

    user = User.query.get_or_404(user_id)

    # Prevent admin from deleting their own account
    if user.id == current_user.id:
        flash("You cannot delete your own account.", "warning")
        return redirect(url_for("admin.admin_dashboard"))

    # Delete related history and messages first
    History.query.filter_by(user_id=user.id).delete()
    Message.query.filter_by(user_id=user.id).delete()

    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully.", "success")

    return redirect(url_for("admin.admin_dashboard"))