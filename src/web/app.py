from flask import Flask
from flask_session import Session

from web.general.routes import Routes as GeneralRoutes


class App:
    @staticmethod
    def main():
        app = Flask(__name__)
        app.config["SESSION_PERMANENT"] = False
        app.config["SESSION_TYPE"] = "filesystem"
        Session(app)
        app.register_blueprint(GeneralRoutes.blueprint)
        app.run()


if __name__ == '__main__':
    App.main()
