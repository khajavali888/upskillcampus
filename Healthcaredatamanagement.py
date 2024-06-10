from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
from datetime import datetime
import random
import time

# Database configuration
DB_HOST = 'your-rds-endpoint'
DB_PORT = '3306'
DB_USER = 'your-username'
DB_PASSWORD = 'your-password'
DB_NAME = 'healthcare'

# Create a database engine
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Create a base class for our classes definitions.
Base = declarative_base()

class Patient(Base):
    _tablename_ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    address = Column(Text, nullable=False)

class MedicalRecord(Base):
    _tablename_ = 'medical_records'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, nullable=False)
    diagnosis = Column(Text, nullable=False)
    treatment = Column(Text, nullable=False)
    record_date = Column(DateTime, default=datetime.utcnow)

class ImagingMetadata(Base):
    _tablename_ = 'imaging_metadata'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, nullable=False)
    image_type = Column(String(50), nullable=False)
    image_path = Column(Text, nullable=False)
    upload_date = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Adding example patient data
new_patient = Patient(name='John Doe', age=30, gender='Male', address='123 Main St')
session.add(new_patient)
session.commit()

# Adding example medical record
new_record = MedicalRecord(patient_id=new_patient.id, diagnosis='Flu', treatment='Rest and hydration')
session.add(new_record)
session.commit()

# Adding example imaging metadata
new_imaging = ImagingMetadata(patient_id=new_patient.id, image_type='X-ray', image_path='/path/to/xray/image.jpg')
session.add(new_imaging)
session.commit()

print("Example data added successfully.")

# Function to simulate IoT data ingestion
def simulate_iot_data(patient_id, interval=5):
    while True:
        temp = random.uniform(36.0, 37.5)  # Simulate temperature data
        bp_systolic = random.randint(110, 140)  # Simulate blood pressure systolic
        bp_diastolic = random.randint(70, 90)  # Simulate blood pressure diastolic

        # Simulate inserting IoT data into a hypothetical table
        print(f"Patient ID: {patient_id}, Temp: {temp}, BP: {bp_systolic}/{bp_diastolic}")

        time.sleep(interval)

# Start IoT data simulation for patient with ID 1
simulate_iot_data(patient_id=1)