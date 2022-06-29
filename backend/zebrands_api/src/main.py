from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5433/zebrands"
db = SQLAlchemy(app)


class Brands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    products = db.relationship("Products")


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sku = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"))


class UsersTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey("users_types.id"))


db.create_all()


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
