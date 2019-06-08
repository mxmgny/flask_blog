from flask import Blueprint

bp = Blueprint('templates', __name__, template_folder='templates')

from app.errors import handlers