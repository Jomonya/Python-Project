#Estate Manager CLI Application
##Overview
This project implements a Command Line Interface (CLI) application using Python and SQLAlchemy ORM for managing properties, tenants, maintenance requests, and contacts within an estate management system.

##Features
Add, List, and Delete Operations:

Add new properties with details such as address, price, description, and image URL.
Add tenants to properties.
Add maintenance requests linked to specific properties.
Add contacts associated with properties.
Listing Information:

View a list of all properties with detailed information, including tenants, maintenance requests, and contacts.
List tenants, maintenance requests, and contacts for a specific property.
Deleting Operations:

Delete properties, tenants, maintenance requests, and contacts.

#Installation
Clone the repository:
git clone <repository_url>
cd estate_manager

##Install dependencies:
bash
pip install -r requirements.txt

##Database Setup:
Ensure you have a database server running (MySQL, PostgreSQL, SQLite,.).
Update config.py with your database credentials and settings.

##Initialize Database:
Run the following commands to initialize the database schema and populate it with sample data (if applicable):

bash
python3 initialize_database.py
Usage
Command Line Interface
Use the following commands to interact with the application:

##Adding a Property:
bash
python3 cli.py add-property "<address>" --price <price> --description "<description>" --image-url "<image_url>"

##Listing Properties:
bash
python3 cli.py list-properties

##Adding a Tenant:
bash
python3 cli.py add-tenant <property_id> "<tenant_name>"

##Listing Tenants:
bash
python3 cli.py list-tenants <property_id>

##Deleting a Property:
bash
python3 cli.py delete-property <property_id>

##Deleting a Tenant:
bash
python3 cli.py delete-tenant <tenant_id>

##Adding a Maintenance Request:
bash
python3 cli.py add-maintenance-request <property_id> "<description>"

##Listing Maintenance Requests:
bash
python3 cli.py list-maintenance-requests <property_id>

##Deleting a Maintenance Request:
bash
python3 cli.py delete-maintenance-request <request_id>

##Adding a Contact:
bash
python3 cli.py add-contact <property_id> "<contact_name>" "<phone>" "<email>" "<role>"

##Listing Contacts:
bash
python3 cli.py list-contacts <property_id>

##Deleting a Contact:
bash
python3 cli.py delete-contact <contact_id>

##Note:
Replace <property_id>, <tenant_id>, <request_id>, <contact_id> with actual IDs from the database.
Enclose parameters containing spaces or special characters in double quotes (").
Ensure your Python environment has necessary dependencies installed (click, sqlalchemy, 
).
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.


Adjust the sections and commands based on the specifics of your application and how you've structured your CLI commands and SQLAlchemy ORM models. Ensure to include any additional setup instructions, customization options, or troubleshooting tips relevant to your project. This README serves as a comprehensive guide for users and contributors to understand, use, and collaborate on your Estate Manager CLI Application effectively.