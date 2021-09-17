import flask
from infrastructure.view_modifiers import response
import services.poem_service as poem_service

blueprint = flask.Blueprint('poets', __name__, template_folder='templates')


@blueprint.route('/poets')
@response(template_file='poets/details.html')
def index():
    return {}

@blueprint.route('/poets/<poet_name>')
#@response(template_file='poets/details.html')
def poets_details(poet_name: str):
    return "Details on poet {}".format(poet_name)

@blueprint.route('/<int:rank>')
#@response(template_file='poets/details.html')
def popular(rank: int):
    return "Details on the {}th most popular poems of the month. ".format(rank)