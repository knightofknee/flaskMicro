from flask import Flask, render_template, request, session, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test4.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)
CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    value = db.Column(db.String(240), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=False, nullable=False)
    def __repr__(self):
        return '<Entry %r>' % self.name
db.create_all()

app.secret_key = b'\x16\xd9\xbf\xb4\xa2w\xd4\xda\xc5I4\xaf\xdc\x11\xd4\xc6'

@app.route('/')
def landing():
  if 'username' in session:
    return redirect(url_for('home'))
  else:
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    selectedUser = User.query.filter_by(username=request.values.get('username')).first()
    if bcrypt.check_password_hash(selectedUser.password, request.values.get('password')):
        session['username'] = request.values.get('username')
        return redirect(url_for('landing'))
    else:
      abort(401)

@app.route('/signup', methods=['POST'])
def signup():
    existsAlready = User.query.filter_by(username=request.values.get('username')).first()
    if existsAlready:
        abort(401)
    else:
      newUser = User(username=request.values.get('username'), password=bcrypt.generate_password_hash(request.values.get('password')).decode('utf-8'))
      db.session.add(newUser)
      db.session.commit()
      session['username'] = request.values.get('username')
      return redirect(url_for('landing'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('landing'))

@app.route('/home')
def home():
    if 'username' in session:
      return render_template('index.html')
    else:
      return redirect(url_for('landing'))

@app.route('/getpairs')
def getpairs():
    result = Entry.query.filter_by(name=request.args.get('key'), username=session['username']).first()
    if result == None:
      return 'No such key found'
    return 'Value: ' + result.value

@app.route('/setpairs', methods=['POST'])
def setpairs():
    existsAlready = Entry.query.filter_by(name=request.values.get('key'), username=session['username']).first()
    response = ''
    if existsAlready == None:
      newPair = Entry(name=request.values.get('key'), value=request.values.get('value'), username=session['username'])
      db.session.add(newPair)
      db.session.commit()
      response = 'Value added'
    else:
      existsAlready.value = request.values.get('value')
      db.session.commit()
      response = 'Value Overwritten'
    return response
