from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def get_eventlog():
    return "Hello"