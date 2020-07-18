from backend.config import BaseConfig
from flask import Flask
import pathlib

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

class Webserver(object):
    def __init__(self):
        self.server = Flask(__name__)
        self.server.config.from_object(BaseConfig())
        self.server.debug = self.server.config["DEBUG"]

    def _start(self):
        print("* Starting webserver ...")
        self.__init_third_party()
        print("* Third party configured ...")
        self.__init_views()
        print("* Views configured and initalized ...")
        self.__init_db_modules()
        print("* Database mapping applied ...")
        self.__update_jinja()
        print("* Jinja2 updated ...")
        self.__webpack_to_jinja()
        print("* Jinja2 extended ...")
        print("* Application ready for use ...")
        return self.server

    def __init_third_party(self):
        """
        This method initializes third party modules.
        """
        db.init_app(self.server)
        migrate.init_app(self.server, db)
        cors.init_app(app=self.server, resources={
            r"/api/*": {"origins": "*"},
            r"/*": {"origins": "http://localhost:5000"},
            r"/*": {"origins": "http://127.0.0.1:5000"}
        }, expose_headers='X-Total-Count')
        
    def __init_views(self):
        """
        This method keeps track of all the available views.
        Every view is a class which needs to be injected into the webserver
        before the view is available to visit.
        """
        from backend.views.index import IndexView
        IndexView.register(self.server, route_base='/')

    def __init_db_modules(self):
        """
        This class initializes the database models mapped with sqlalchemy.
        If a module is not directly called in a view the module will not be
        available. This kind of situations are rare but do happen.
        When your module is not available / finable by flask it will not migrate.
        Therefor we call those modules here.
        """
        pass

    def __update_jinja(self):
        """
        Updates jinja with custom python commands. Each new command will be callable
        in the jinja templates.
        """
        from backend._jinja import CustomFunctions
        self.server.jinja_env.globals.update(
            datenow=CustomFunctions.datenow,
            get_debug_value=CustomFunctions.get_debug_bool,
        )

    def _get_pathlib(self, *args):
        return pathlib.Path(pathlib.Path(__file__).resolve().parent, *args)

    def __webpack_to_jinja(self):
        """Intergrate webpack into jinja2 render template"""
        from jinja2_webpack import Environment as WebpackEnvironment
        from jinja2_webpack.filter import WebpackFilter
        # Time to load in NPM manifest
        try:
            manifest = self._get_pathlib('static', 'react', 'manifest.json')
            if not manifest.is_file():
                with open(str(manifest), 'w') as f: f.write("{}")
            webpack_env = WebpackEnvironment(manifest=str(pathlib.PurePosixPath(manifest)), publicRoot='')
            self.server.jinja_env.filters['webpack'] = WebpackFilter(webpack_env)
        except FileNotFoundError: raise FileNotFoundError('The frontend needs to be compiled first')
