from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random

db = SQLAlchemy()  # Initialize SQLAlchemy
fake = Faker()  # Create a Faker instance

class Landlord(db.Model):
    """Model for landlords."""
    __tablename__ = 'landlords'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    properties = db.relationship('Property', backref='landlord', lazy=True)
    tenants = db.relationship('Tenant', secondary='leases', backref='landlords', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'properties': [property.id for property in self.properties],
            'tenants': [tenant.id for tenant in self.tenants]
        }

class Property(db.Model):
    """Model for properties."""
    __tablename__ = 'properties'
    
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(150), nullable=False)
    landlord_id = db.Column(db.Integer, db.ForeignKey('landlords.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'address': self.address,
            'landlord_id': self.landlord_id
        }

class Tenant(db.Model):
    """Model for tenants."""
    __tablename__ = 'tenants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    due_amount = db.Column(db.Float, nullable=False, default=0.0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'due_amount': self.due_amount
        }

class Lease(db.Model):
    """Model for the lease association between tenants and properties."""
    __tablename__ = 'leases'
    
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)

def initialize_db():
    """Initialize the database with sample data."""
    db.create_all()  # Create all tables

    if Landlord.query.count() == 0:  # Only add data if the table is empty
        # Create 5 fake landlords
        landlords = []
        for _ in range(5):
            landlord = Landlord(name=fake.name())
            landlords.append(landlord)
            db.session.add(landlord)

        # Commit the landlords to the database
        db.session.commit()

        # Create fake properties and tenants
        for landlord in landlords:
            for _ in range(random.randint(1, 3)):  # Random number of properties (1-3) per landlord
                property = Property(address=fake.address(), landlord=landlord)
                db.session.add(property)

                for _ in range(random.randint(1, 2)):  # Random number of tenants (1-2) per property
                    tenant = Tenant(name=fake.name(), due_amount=random.uniform(300, 1000))
                    db.session.add(tenant)

                    # Create lease relationships
                    lease = Lease(tenant=tenant, property=property)
                    db.session.add(lease)

        # Commit all changes to the database
        db.session.commit()
