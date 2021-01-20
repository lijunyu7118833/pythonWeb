from application import app
from web.controller.login.login import route_user

from web.controller.article.article import route_article

app.register_blueprint(route_user, url_prefix="/user")
app.register_blueprint(route_article, url_prefix="/article")
