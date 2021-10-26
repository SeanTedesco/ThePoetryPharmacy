import sys
sys.path.append('../')
import flask
import os
import thepoetrypharmacy_com.data.db_session as db_session

app = flask.Flask(__name__)

def main():
    register_blueprints()
    db_init()
    app.run(debug=True)

def register_blueprints():
    from views import home_view, poets_view, acount_view
    app.register_blueprint(home_view.blueprint)
    app.register_blueprint(poets_view.blueprint)
    app.register_blueprint(acount_view.blueprint)

def db_init():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pharm.sqlite'
    )
    db_session.global_init(db_file)
    
if __name__ == '__main__':
    main()