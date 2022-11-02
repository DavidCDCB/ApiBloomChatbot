from flask import Flask
from flask_cors import CORS
from routes.User_routes import user_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(user_routes)


# https://docs.deta.sh/docs/micros/getting_started/#creating-your-first-micro
# https://www-rahulvk-com.translate.goog/how-to-host-your-flask-app-website-for-free/?_x_tr_sl=auto&_x_tr_tl=es&_x_tr_hl=es
if __name__ == '__main__':
	app.run()
