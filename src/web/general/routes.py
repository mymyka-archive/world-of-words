from flask import Blueprint


class Routes:
    blueprint: Blueprint = Blueprint(
        name='general',
        import_name=__name__,
        static_folder='static',
        template_folder='templates'
    )

    @blueprint.route('/')
    @staticmethod
    def index():
        return "Hello"
