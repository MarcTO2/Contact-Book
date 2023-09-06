import pytest
from .. import contact_book  # Import your main script

# Define fixture to set up and tear down the database for testing
@pytest.fixture
def setup_teardown_database():
    # Create the database and tables
    contact_book.create_database()
    yield
    # Optionally, you can add cleanup code here if needed

# Test add_contact function
def test_add_contact(setup_teardown_database):
    # Test adding a contact
    contact_book.add_contact("John Doe", "john@example.com", "123-456-7890", "Friends")

    # Assert that the contact was added
    assert contact_book.list_contacts() == "List of Contacts:\nID: 1, Name: John Doe, Email: john@example.com, Phone: 123-456-7890, Category: Friends"

# You can add more test cases for other functions (list_contacts, delete_contact, edit_contact, search_contact) in a similar manner.

# Test list_contacts function
def test_list_contacts(setup_teardown_database):
    # Test listing contacts when there are no contacts
    assert contact_book.list_contacts() == "No contacts found."

# Test delete_contact function
def test_delete_contact(setup_teardown_database):
    # Test deleting a contact
    contact_book.add_contact("Alice Smith", "alice@example.com", "987-654-3210", "Family")
    contact_book.delete_contact(1)
    
    # Assert that the contact was deleted
    assert contact_book.list_contacts() == "No contacts found."

# Test edit_contact function
def test_edit_contact(setup_teardown_database):
    # Test editing a contact
    contact_book.add_contact("Bob Johnson", "bob@example.com", "555-555-5555", "Work")
    contact_book.edit_contact(1, "Bob Johnson Updated", "updated@example.com", "111-111-1111", "Friends")
    
    # Assert that the contact was edited
    assert contact_book.list_contacts() == "List of Contacts:\nID: 1, Name: Bob Johnson Updated, Email: updated@example.com, Phone: 111-111-1111, Category: Friends"

# Test search_contact function
def test_search_contact(setup_teardown_database):
    # Test searching for a contact
    contact_book.add_contact("Charlie Brown", "charlie@example.com", "777-777-7777", "Work")
    result = contact_book.search_contact("Charlie")
    
    # Assert that the search result contains the contact
    assert "Charlie Brown" in result
    assert "charlie@example.com" in result

if __name__ == "__main__":
    pytest.main()

