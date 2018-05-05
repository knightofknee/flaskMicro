from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.cors import CORS, cross_origin
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)

# cors = CORS(app, resources={r"/": {"origins": "http://localhost:5000"}})
CORS(app)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    value = db.Column(db.String(240), unique=False, nullable=False)

    # def __init__(self, name=None, value=None):
    #     self.name = name
    #     self.value = value

    def __repr__(self):
        return '<Entry %r>' % self.name

db.create_all()

@app.route('/')
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def index():
    return render_template('index.html')
    # if 'username' in session:
    #     return 'Logged in as %s' % escape(session['username'])
    # return 'You are not logged in'
@app.route('/login')
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def login():
    return render_template('login.html')

@app.route('/getpairs')
def getpairs():
    result = Entry.query.filter_by(name=request.args.get('key')).first()
    if result == None:
      return 'No such key found'
    return result.value

@app.route('/setpairs', methods=['POST'])
def setpairs():
    existsAlready = Entry.query.filter_by(name=request.values.get('key')).first()
    if existsAlready == None:
      newPair = Entry(name=request.values.get('key'), value=request.values.get('value'))
      db.session.add(newPair)
      db.session.commit()
    else:
      existsAlready.value = request.values.get('value')
      db.session.commit()
    return 'success!'

    # pip install -U flask-cors
    # install this, try comment line 2 and 4, then try the others if that fails
    # if both fail, try response = flask.jsonify({'some': 'data'})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response

    # what should setpairs return???
