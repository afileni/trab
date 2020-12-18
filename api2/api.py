from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
#from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://<mysql_username>:<mysql_password>@<mysql_host>:<mysql_port>/<mysql_db>'
#dialect+driver://username:password@host:port/database
#app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:senhaFiap@127.0.0.1:3306/fiap'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'fiap'
app.config['MYSQL_DATABASE_DB'] = 'fiapdb'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1:3306'
db = SQLAlchemy(app)

###Models####
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    productDescription = db.Column(db.String(100))
    productBrand = db.Column(db.String(20))
    price = db.Column(db.Integer)

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,title,productDescription,productBrand,price):
        self.title = title
        self.productDescription = productDescription
        self.productBrand = productBrand
        self.price = price
    def __repr__(self):
        return '' % self.id
db.create_all()

#class ProductSchema(ModelSchema):
#    class Meta(ModelSchema.Meta):
#        model = Product
#        sqla_session = db.session
#    id = fields.Number(dump_only=True)
#    title = fields.String(required=True)
#    productDescription = fields.String(required=True)
#    productBrand = fields.String(required=True)
#    price = fields.Number(required=True)
 
@app.route('/products', methods = ['GET'])
def index():
    get_products = Product.query.all()
    #product_schema = ProductSchema(many=True)
    #products = product_schema.dump(get_products)
    return make_response(jsonify({"product": products}))
    
