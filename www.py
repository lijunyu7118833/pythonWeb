from application import app
from web.controller.login.login import route_user


app.register_blueprint(route_user, url_prefix="/user")
