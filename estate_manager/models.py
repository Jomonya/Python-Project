from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Property model
class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    address = Column(String(255), nullable=False)
    price = Column(Integer)
    description = Column(String(255))
    image_url = Column(String(255))  

    # One-to-many relationship with Tenant
    tenants = relationship('Tenant', back_populates='property', cascade='all, delete-orphan')

    # One-to-many relationship with MaintenanceRequest
    maintenance_requests = relationship('MaintenanceRequest', back_populates='property', cascade='all, delete-orphan')

    # One-to-many relationship with Contact
    contacts = relationship('Contact', back_populates='property', cascade='all, delete-orphan')

# Tenant model
class Tenant(Base):
    __tablename__ = 'tenants'

    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('properties.id'))
    name = Column(String(100), nullable=False)

    property = relationship('Property', back_populates='tenants')

# MaintenanceRequest model
class MaintenanceRequest(Base):
    __tablename__ = 'maintenance_requests'

    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('properties.id'))
    description = Column(String(255), nullable=False)
    request_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default='Pending')  

    property = relationship('Property', back_populates='maintenance_requests')

# Contact model
class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('properties.id'))
    name = Column(String(100), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    role = Column(String(100))

    property = relationship('Property', back_populates='contacts')

# Database initialization
def init_db():
    engine = create_engine('sqlite:///real_estate.db')
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=create_engine('sqlite:///real_estate.db'))
