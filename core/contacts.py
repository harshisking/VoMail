import sqlite3
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
DB_FILE = os.getenv("DB_FILE", "db/contacts.db")  # fallback to contacts.db
db_path = os.path.dirname(DB_FILE)
if db_path and not os.path.exists(db_path):
    os.makedirs(db_path)

conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
conn = sqlite3.connect(":memory:")
c = conn.cursor()

#the functions start

def create_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  alias TEXT,
                  email TEXT
                  )''')



def add_contact(alias: str, email: str):
    while True:
        try:
            with conn:
                c.execute("INSERT INTO contacts (alias,email) VALUES (:alias,:email)", {'alias': alias, 'email': email})
            print("Contact Saved with ID:", c.lastrowid)
            break
        except sqlite3.OperationalError:
            create_table()




def get_contact(alias: str):
    while True:
        try:
            c.execute('SELECT * FROM contacts WHERE alias=:alias', {'alias':alias})
            result = c.fetchone()
            return result
        except :
            print(f"No Contact Found with alias {alias}")
            break




def update_contact(alias: str, new_email: str):
    while True:
        try:
            with conn:
                c.execute('UPDATE contacts SET email=:email WHERE alias=:alias', {'email':new_email,'alias':alias})
            print(f"Contact with {alias} updated to {new_email}")
            break
        except:
            print(f"No contact found with alias {alias}")
            break




def remove_contact(alias: str):
    while True:
        try:
            a = input(f"ARE YOU SURE TO REMOVE {alias} (y/n):")
            if a.lower() == 'y':
                with conn:
                    c.execute('DELETE FROM contacts WHERE alias=:alias', {'alias':alias})
                print("Contact successfully removed")
                break
            else:
                print(f"{alias} not removed")
        except:
            print("Contact not found")
            break




def list_contacts():
    try:
        c.execute('SELECT * FROM contacts')
        return c.fetchall()
    except:
        print("First add some contacts")