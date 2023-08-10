import sqlite3


def create_sqlite_db():
    conn = sqlite3.connect('hn.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE hn (
            hn_id text,
            timestamp text,
            author text,
            title text,
            text text,
            descendants int,
            score int,
            url text
        )
    ''')
    conn.commit()
    conn.close()


def insert_into_sqlite_db(data):

    conn = sqlite3.connect('hn.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO hn VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?
        )
    ''', data)
    conn.commit()
    conn.close()


fake_data = [
    ('1', '2021-01-01', 'author1', 'title1', 'text1', 1, 1, 'url1'),
    ('2', '2021-01-02', 'author2', 'title2', 'text2', 2, 2, 'url2'),
    ('3', '2021-01-03', 'author3', 'title3', 'text3', 3, 3, 'url3'),
]



create_sqlite_db()
for data in fake_data:
    insert_into_sqlite_db(data)

def sqlite_scan(db, table):
    # query individual tables using the sqlite_scan function.
    # SELECT * FROM sqlite_scan('hn.db', 'hn'); 
    return f"sqlite_scan('{db}', '{table}')"
