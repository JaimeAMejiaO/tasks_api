from flask import Flask, render_template
from dotenv import load_dotenv
import os

from config.mongodb import mongo
from routes.task_routes import task

load_dotenv()

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(task, url_prefix='/task')

if __name__ == '__main__':
    app.run(debug=True)  