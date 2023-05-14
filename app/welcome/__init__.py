from flask import Blueprint

# Every route which contains "/auth" will be redirected to this blueprint
greetings = Blueprint('greetings', __name__, url_prefix='/greetings')

# It has to be here because it comes after creating the blueprint
from . import views