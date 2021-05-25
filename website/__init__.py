from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import datetime

db = SQLAlchemy()
DB_NAME = "novus.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, Transaction

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    from .models import User, Note, Transaction

    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
        data = [{'amount':6086.15,'currency':"CNY",'sender':"DE36 9083 7042 7820 6733 86",'receiver':"DE24 0760 1020 0268 1947 87"},
            {"amount":4917.45,"currency":"COP","sender":"SI04 6724 3315 4472 160","receiver":"FR77 9686 0386 77TV ZWA2 3QUE C30"},
            {"amount":4959.65,"currency":"EUR","sender":"CY75 9515 9198 WEJA WYSP 3FRR UBMS","receiver":"PS96 RLRF JSZU LPUW 4LWK WE7A DSZJ C"},
            {"amount":2689.8,"currency":"MKD","sender":"MC35 6982 9145 54GM W49X EJ96 D84","receiver":"AE74 8921 1951 1665 4429 820"},
            {"amount":4464.61,"currency":"CNY","sender":"GL64 1258 1828 4453 84","receiver":"FR09 5219 0287 07SC QFJH UVVS T92"},
            {"amount":8255.9,"currency":"EUR","sender":"BG79 GXUS 4242 20XP BSCV OK","receiver":"CY75 6321 1148 RIOC EFVZ HT2Y JUMB"},
            {"amount":8670.4,"currency":"LAK","sender":"RO91 SULG NT7Z DR3E 2HNR EHGD","receiver":"HR78 6633 3432 2772 8784 7"},
            {"amount":521.83,"currency":"PLN","sender":"IS04 7675 4259 8543 8110 6484 20","receiver":"MK54 686C 2OGK ILJR R99"},
            {"amount":479.34,"currency":"CNY","sender":"PK75 LCJT U6DK G4WW RMU6 9ELB","receiver":"BG82 SKJK 9550 40JN HLYI RX"},
            {"amount":6151.67,"currency":"CNY","sender":"BH56 YJQG 8YVO CCTX PSZC RA","receiver":"IT68 Q762 8240 609E AG4W UX3D F7G"}]

        with app.app_context():
            for entry in data:
                row = Transaction(amount=entry["amount"],currency=entry["currency"],date=datetime.datetime.now(),sender=entry["sender"],receiver=entry["receiver"])
                db.session.add(row)
                db.session.commit()
