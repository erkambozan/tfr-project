import sqlite3


def create_table():
    connection = sqlite3.connect('database/school.db')  # file path
    # create a cursor object from the cursor class
    cur = connection.cursor()

    cur.execute('''
       CREATE TABLE locations (
            id UUID PRIMARY KEY,
            fsq_id UUID,
            latitude REAL,
            longitude REAL,
            address TEXT,
            country TEXT,
            region TEXT,
            name TEXT
        )
    ''')

    print("\nDatabase created successfully!!!")
    # committing our connection
    connection.commit()

    # close our connection
    connection.close()
