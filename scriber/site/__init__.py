from flask import Blueprint


bp = Blueprint('site', __name__)

from scriber.site import routes