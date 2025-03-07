import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    # instance_relative_config=True tells the app that configuration files are relative to
    # the instance folder. The instance folder shouldn’t be committed to git.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # To be overridden in prod
        SECRET_KEY='dev',
        # database config
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config under instance folder, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    # This ensures both / and /blog will direct to index page.
    app.add_url_rule('/', endpoint='index')

    return app
