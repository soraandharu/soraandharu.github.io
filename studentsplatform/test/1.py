from peewee import *

db = SqliteDatabase('example.db')

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True, primary_key=True)  # Use CharField with primary_key=True
    email = CharField(unique=True)  


def initialize_db():
    db.connect()
    db.create_tables([User], safe=True)
    print("Database initialized and tables created.")

if __name__ == '__main__':
    initialize_db()
    # Example usage

    user = User.create(username='john_doe', email='john@example.com')