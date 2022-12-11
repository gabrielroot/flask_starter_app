from flask import render_template, Blueprint

user_routes = Blueprint('user_routes', __name__, url_prefix='/user', template_folder='templates/user')

@user_routes.route('/')
def index():
    return render_template('user/index.html')