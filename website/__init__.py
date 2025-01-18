from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Dyyjkhfd'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/artemiscash.github.io/sustain/')
    app.register_blueprint(auth, url_prefix='/artemiscash.github.io/sustain/')


    return app
