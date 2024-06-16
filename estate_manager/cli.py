import click
from models import Session, Property, Tenant, MaintenanceRequest, Contact

@click.group()
def cli():
    pass

@click.command()
@click.argument('address')
@click.option('--price', type=int, default=0, help='Price of the property')
@click.option('--description', default='', help='Description of the property')
@click.option('--image-url', default='', help='Image URL of the property')
def add_property(address, price, description, image_url):
    """Add a new property."""
    session = Session()
    property = Property(address=address, price=price, description=description, image_url=image_url)
    session.add(property)
    session.commit()
    click.echo(f'Property {address} added.')
    session.close()

@click.command()
@click.argument('property_id', type=int)
@click.argument('image_url')
def add_property_image(property_id, image_url):
    """Add an image URL to a property."""
    session = Session()
    property = session.get(Property, property_id)
    if property:
        property.image_url = image_url
        session.commit()
        click.echo(f'Image URL added to property {property.address}.')
    else:
        click.echo('Property not found.')
    session.close()

@click.command()
def list_properties():
    """List all properties with their details."""
    session = Session()
    properties = session.query(Property).all()
    for property in properties:
        click.echo(f'ID: {property.id}, Address: {property.address}, Price: {property.price}, Description: {property.description}, Image URL: {property.image_url}')
        click.echo('Tenants:')
        for tenant in property.tenants:
            click.echo(f'  Tenant ID: {tenant.id}, Name: {tenant.name}')
        click.echo('Maintenance Requests:')
        for request in property.maintenance_requests:
            click.echo(f'  Request ID: {request.id}, Description: {request.description}, Status: {request.status}')
        click.echo('Contacts:')
        for contact in property.contacts:
            click.echo(f'  Contact ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Role: {contact.role}')
    session.close()

@click.command()
@click.argument('property_id', type=int)
@click.argument('name')
def add_tenant(property_id, name):
    """Add a new tenant to a property."""
    session = Session()
    property = session.get(Property, property_id)
    if property:
        tenant = Tenant(name=name, property=property)
        session.add(tenant)
        session.commit()
        click.echo(f'Tenant {name} added to property {property.address}.')
    else:
        click.echo('Property not found.')
    session.close()

@click.command()
@click.argument('property_id', type=int)
def list_tenants(property_id):
    """List all tenants of a property."""
    session = Session()
    property = session.get(Property, property_id)
    if property:
        tenants = session.query(Tenant).filter_by(property_id=property_id).all()
        for tenant in tenants:
            click.echo(f'{tenant.id}: {tenant.name}')
    else:
        click.echo('Property not found.')
    session.close()

@click.command()
@click.argument('property_id', type=int)
def delete_property(property_id):
    """Delete a property and all its tenants."""
    session = Session()
    property = session.get(Property, property_id)
    if property:
        session.delete(property)
        session.commit()
        click.echo(f'Property {property.address} and all its tenants deleted.')
    else:
        click.echo('Property not found.')
    session.close()

@click.command()
@click.argument('tenant_id', type=int)
def delete_tenant(tenant_id):
    """Delete a tenant."""
    session = Session()
    tenant = session.get(Tenant, tenant_id)
    if tenant:
        session.delete(tenant)
        session.commit()
        click.echo(f'Tenant {tenant.name} deleted.')
    else:
        click.echo('Tenant not found.')
    session.close()

@click.command()
@click.argument('property_id', type=int)
@click.argument('description')
def add_maintenance_request(property_id, description):
    """Add a new maintenance request to a property."""
    session = Session()
    maintenance_request = MaintenanceRequest(property_id=property_id, description=description)
    session.add(maintenance_request)
    session.commit()
    session.close()
    click.echo(f'Maintenance request added to property {property_id}.')

@click.command()
@click.argument('property_id', type=int)
def list_maintenance_requests(property_id):
    """List all maintenance requests of a property."""
    session = Session()
    property = session.get(Property, property_id)
    if property:
        maintenance_requests = session.query(MaintenanceRequest).filter_by(property_id=property_id).all()
        for request in maintenance_requests:
            click.echo(f'{request.id}: {request.description} (Status: {request.status})')
    else:
        click.echo('Property not found.')
    session.close()

@click.command()
@click.argument('request_id', type=int)
def delete_maintenance_request(request_id):
    """Delete a maintenance request."""
    session = Session()
    request = session.get(MaintenanceRequest, request_id)
    if request:
        session.delete(request)
        session.commit()
        click.echo(f'Maintenance request {request.description} deleted.')
    else:
        click.echo('Maintenance request not found.')
    session.close()

@click.command()
@click.argument('property_id', type=int)
@click.argument('name')
@click.argument('phone')
@click.argument('email')
@click.argument('role')
def add_contact(property_id, name, phone, email, role):
    """Add a new contact to a property."""
    session = Session()
    contact = Contact(property_id=property_id, name=name, phone=phone, email=email, role=role)
    session.add(contact)
    session.commit()
    session.close()
    click.echo(f'Contact {name} added to property {property_id}.')

@click.command()
@click.argument('property_id', type=int)
def list_contacts(property_id):
    """List all contacts of a property."""
    session = Session()
    property = session.get(Property, property_id)
    if property:
        contacts = session.query(Contact).filter_by(property_id=property_id).all()
        for contact in contacts:
            click.echo(f'{contact.id}: {contact.name} (Role: {contact.role}, Phone: {contact.phone}, Email: {contact.email})')
    else:
        click.echo('Property not found.')
    session.close()

@click.command()
@click.argument('contact_id', type=int)
def delete_contact(contact_id):
    """Delete a contact."""
    session = Session()
    contact = session.get(Contact, contact_id)
    if contact:
        session.delete(contact)
        session.commit()
        click.echo(f'Contact {contact.name} deleted.')
    else:
        click.echo('Contact not found.')
    session.close()

# Register commands with the CLI group
cli.add_command(add_property)
cli.add_command(add_property_image)
cli.add_command(list_properties)
cli.add_command(add_tenant)
cli.add_command(list_tenants)
cli.add_command(delete_property)
cli.add_command(delete_tenant)
cli.add_command(add_maintenance_request)
cli.add_command(list_maintenance_requests)
cli.add_command(delete_maintenance_request)
cli.add_command(add_contact)
cli.add_command(list_contacts)
cli.add_command(delete_contact)

if __name__ == '__main__':
    cli()
