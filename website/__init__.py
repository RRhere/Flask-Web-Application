import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()
DB_NAME = "temp1.db"

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    db.init_app(app)
    mail.init_app(app)

    from .views import views as views_blueprint
    from .auth import auth as auth_blueprint
    
    app.register_blueprint(views_blueprint, url_prefix='/')
    app.register_blueprint(auth_blueprint, url_prefix='/')
    
    from .models import User

    with app.app_context():
        if not os.path.exists(os.path.join('website', DB_NAME)):
            db.create_all()
            print('Created Database!')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
