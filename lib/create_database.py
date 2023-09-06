from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy engine for the SQLite database
engine = create_engine('sqlite:///contacts.db')

# Define a base class for declarative models
Base = declarative_base()

# Define the Category model
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Define the Contact model
class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))

# Create the database and tables
def create_database():
    Base.metadata.create_all(engine)
    print("Database created.")

if __name__ == "__main__":
    create_database()
