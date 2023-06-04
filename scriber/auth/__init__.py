from flask import Blueprint

bp = Blueprint('auth', __name__)

from scriber.auth import routes