from flask import Flask

from web.general.routes import Routes as GeneralRoutes


class App:
    @staticmethod
    def main():
        app = Flask(__name__)
        app.register_blueprint(GeneralRoutes.blueprint)
        app.run()


if __name__ == '__main__':
    App.main()
