import os
from flask import Flask
from flask.ext.cors import CORS

#from flask.ext.bootstrap import Bootstrap
#from flask.ext.sqlalchemy import SQLAlchemy

#bootstrap = Bootstrap()
#db = SQLAlchemy()

def create_app(config_name):
    """Create an application instance."""
    app = Flask(__name__)

    # import configuration
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_pyfile(cfg)

    # initialize extensions
    #bootstrap.init_app(app)
    #db.init_app(app)
    cors = CORS(app)

    # modules
    from app.modules.store.controllers import mod_store as store_module

    app.register_blueprint(store_module)

    @app.after_request
    def after_request(response):
      response.headers.add('Access-Control-Allow-Origin', '*')
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
      return response

    return app