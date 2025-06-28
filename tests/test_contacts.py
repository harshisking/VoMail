### Using AI to get this script.


import sys
import os
from dotenv import load_dotenv
import os
import sys

# Load test environment variables from .env.test
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env.test'))

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core import contacts

def run_tests():
    print("✅ Running contact system tests...")

    # Reconnect to fresh in-memory DB
    contacts.conn = contacts.sqlite3.connect(":memory:")
    contacts.c = contacts.conn.cursor()
    contacts.create_table()

    # Test 1: Add & Get
    contacts.add_contact("Riya", "riya@example.com")
    result = contacts.get_contact("Riya")
    assert result == "riya@example.com", "❌ Get Contact Failed"

    # Test 2: Update
    contacts.update_contact("Riya", "riya@new.com")
    result = contacts.get_contact("Riya")
    assert result == "riya@new.com", "❌ Update Failed"

    # Test 3: List
    contacts.add_contact("Jay", "jay@example.com")
    all_contacts = contacts.list_contacts()
    assert len(all_contacts) == 2, "❌ List Failed"

    # Test 4: Remove
    # Override confirmation prompt just for testing
    contacts.remove_contact = lambda alias: contacts.c.execute("DELETE FROM contacts WHERE alias=?", (alias,))
    contacts.remove_contact("Riya")
    result = contacts.get_contact("Riya")
    assert result is None, "❌ Remove Failed"

    print("🎉 All tests passed!")

if __name__ == "__main__":
    run_tests()
