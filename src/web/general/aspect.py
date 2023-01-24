from functools import wraps
from flask import session, redirect, request


class Auth:
    @staticmethod
    def auth(endpoint_func):
        @wraps(endpoint_func)
        def wrapper():
            if not session.get("email"):
                return redirect("/signin")
            return endpoint_func()
        return wrapper

    @staticmethod
    def register_session(endpoint_func):
        @wraps(endpoint_func)
        def wrapper():
            if request.method == 'POST':
                session['email'] = request.form.get('email')
            if session.get('email'):
                return redirect('/home')
            return endpoint_func()
        return wrapper
