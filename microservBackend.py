from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)
CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    value = db.Column(db.String(240), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    def __repr__(self):
        return '<Entry %r>' % self.name
db.create_all()

@app.route('/')
def landing():
  if session.get('logged_in'): # add 'not' for logic to be set up again
    return render_template('login.html')
  else:
    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return landing()

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return landing()

@app.route('/home')
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def home():
    return render_template('index.html')
    # if 'username' in session:
    #     return 'Logged in as %s' % escape(session['username'])
    # return 'You are not logged in'
# @app.route('/login')


# def login():
#     return render_template('login.html')

@app.route('/getpairs')
def getpairs():
    result = Entry.query.filter_by(name=request.args.get('key'), username='Brian').first()
    if result == None:
      return 'No such key found'
    return result.value

@app.route('/setpairs', methods=['POST'])
def setpairs():
    existsAlready = Entry.query.filter_by(name=request.values.get('key'), username='Brian').first()
    if existsAlready == None:
      newPair = Entry(name=request.values.get('key'), value=request.values.get('value'), username='Brian')
      db.session.add(newPair)
      db.session.commit()
    else:
      existsAlready.value = request.values.get('value')
      db.session.commit()
    return 'success!'

    # what should setpairs return???
