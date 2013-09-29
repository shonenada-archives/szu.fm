from flask import Flask
from flask.ext.gears import Gears

from szufm.asset import setup_compilers, setup_compressors
from szufm.views.master import master_app


gears = Gears()


def app(import_name=None, config=None):
    app = Flask(import_name or __name__)

    app.config.from_object('szufm.settings')
    if not config:
        app.config.from_pyfile(config)

    gears.init_app(app)
    setup_compressors(app)
    setup_compilers(app)

    app.register_blueprint(master_app)

    return app
