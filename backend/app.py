from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, initialize_db, Landlord, Property, Tenant

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/api/tenants', methods=['GET'])
def get_tenants():
    tenants = Tenant.query.all()
    return jsonify([tenant.to_dict() for tenant in tenants])

@app.route('/api/landlords', methods=['GET'])
def get_landlords():
    landlords = Landlord.query.all()
    return jsonify([landlord.to_dict() for landlord in landlords])

@app.route('/api/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    return jsonify([property.to_dict() for property in properties])

if __name__ == '__main__':
    with app.app_context():
        initialize_db()  # Initialize the database with fake data
    app.run(debug=True)
