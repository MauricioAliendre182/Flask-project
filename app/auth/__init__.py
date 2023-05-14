from flask import Blueprint

# Every route which contains "/auth" will be redirected to this blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')

# It has to be here because it comes after creating the blueprint
from . import views
