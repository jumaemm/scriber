from scriber.site import bp
from flask import render_template

@bp.route('/')
def index():
    return render_template('index.html')