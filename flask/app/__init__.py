import os
from flask import Flask

def create_app(config_name):
    """Create an application instance."""
    app = Flask(__name__)

    # import configuration
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_pyfile(cfg)

    # modules
    from app.modules.ml.ml_controllers import mod_ml as ml_module

    app.register_blueprint(ml_module)

    return app