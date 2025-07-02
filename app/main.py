from flask import Flask
from app.routes import bp
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
app.register_blueprint(bp)

asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
