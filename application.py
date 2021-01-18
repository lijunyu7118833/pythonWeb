from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager




db = SQLAlchemy()


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, static_folder=None)
        self.config.from_pyfile('config/setting.py')
        db.init_app(self)

app = Application(__name__)
manager = Manager(app)
