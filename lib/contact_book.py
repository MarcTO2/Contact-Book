import argparse
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///contacts.db')
Session = sessionmaker(bind=engine)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contacts = relationship("Contact", back_populates="category")

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="contacts")

def create_database():
    Base.metadata.create_all(engine)
    print("Database created.")

def add_contact(name, email, phone, category_name):
    session = Session()
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()
    contact = Contact(name=name, email=email, phone=phone, category=category)
    session.add(contact)
    session.commit()
    print("Contact added.")

def list_contacts():
    session = Session()
    contacts = session.query(Contact).all()
    if not contacts:
        print("No contacts found.")
    else:
        print("List Of Contacts:")
        for contact in contacts:
            print(f"ID: {contact.id}, Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}, Category: {contact.category.name}")

def delete_contact(contact_id):
    session = Session()
    contact = session.query(Contact).filter_by(id=contact_id).first()
    if contact:
        session.delete(contact)
        session.commit()
        print("Contact deleted.")
    else:
        print("Contact not found.")

def edit_contact(contact_id, name, email, phone, category_name):
    session = Session()
    contact = session.query(Contact).filter_by(id=contact_id).first()
    if contact:
        contact.name = name
        contact.email = email
        contact.phone = phone
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            session.add(category)
            session.commit()
        contact.category = category
        session.commit()
        print("Contact edited.")
    else:
        print("Contact not found.")

def search_contact(name):
    session = Session()
    contacts = session.query(Contact).filter(Contact.name.like(f"%{name}%")).all()
    if not contacts:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for contact in contacts:
            print(f"ID: {contact.id}, Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}, Category: {contact.category.name}")

def main():
    parser = argparse.ArgumentParser(description="CLI Contact Book")
    parser.add_argument("command", choices=["create", "add", "list", "delete", "edit", "search"], help="Command to execute")
    
    args = parser.parse_args()

    if args.command == "create":
        create_database()
    elif args.command == "add":
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        category = input("Category: ")
        add_contact(name, email, phone, category)
    elif args.command == "list":
        list_contacts()
    elif args.command == "delete":
        contact_id = int(input("Enter contact ID to delete: "))
        delete_contact(contact_id)
    elif args.command == "edit":
        contact_id = int(input("Enter contact ID to edit: "))
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        category = input("Category: ")
        edit_contact(contact_id, name, email, phone, category)
    elif args.command == "search":
        name = input("Enter name to search: ")
        search_contact(name)

if __name__ == "__main__":
    main()


