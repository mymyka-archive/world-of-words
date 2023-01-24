from flask import Blueprint, render_template, session, redirect, request

from web.general.aspect import Auth


class Routes:
    blueprint: Blueprint = Blueprint(
        name='general',
        import_name=__name__,
        static_folder='static',
        template_folder='templates'
    )

    @staticmethod
    @blueprint.route('/')
    def index():
        return render_template('index.html')

    @staticmethod
    @blueprint.route('/signin', methods=['GET', 'POST'])
    @Auth.register_session
    def sign_in():
        return render_template('signin.html')

    @staticmethod
    @blueprint.route('/home')
    @Auth.auth
    def home():
        return render_template('home.html')
