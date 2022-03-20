import flask
from infrastructure.view_modifiers import response
import services.poem_service as poem_service
from thepoetrypharmacy_com.data import poem

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    poems = poem_service.get_latest_poems(5)
    #poems = poem_service.get_poems_by_author("Allison Adelle Hedge Coke")
    return {'poems': poems}

@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}