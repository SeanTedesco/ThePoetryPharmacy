import flask
from infrastructure.view_modifiers import response
import services.poem_service as poem_service

blueprint = flask.Blueprint('acount', __name__, template_folder='templates')

########################### INDEX ###########################
@blueprint.route('/acount')
@response(template_file='acount/index.html')
def index():
    return {}


########################### REGISTER ###########################
@blueprint.route('/acount/register', methods=['GET'])
@response(template_file='acount/register.html')
def register_get():
    return {}

@blueprint.route('/acount/register', methods=['POST'])
@response(template_file='acount/register.html')
def register_post():
    return {}


########################### LOGIN ###########################
@blueprint.route('/acount/login', methods=['GET'])
@response(template_file='acount/login.html')
def login_get():
    return {}

@blueprint.route('/acount/login', methods=['POST'])
@response(template_file='acount/login.html')
def login_post():
    return {}


########################### LOGOUT ###########################
@blueprint.route('/acount/logout')
def logout():
    return {}