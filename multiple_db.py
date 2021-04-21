from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cats.db'
app.config['SQLALCHEMY_BINDS'] = {'dogs': 'sqlite:///dogs.db',
                                  'humsters': 'sqlite:///others.db'}

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Customer(db.Model):
    __bind_key__ = 'dogs'
    id = db.Column(db.Integer, primary_key=True)


class Category(db.Model):
    __bind_key__ = 'humsters'
    id = db.Column(db.Integer, primary_key = True)


@app.route('/')
def index():
    customer = Customer(id=111)
    db.session.add(customer)
    db.session.commit()

    return 'Added the value to the Customes table for dogs.'


if __name__ == '__main__':
    app.run(debug=True)