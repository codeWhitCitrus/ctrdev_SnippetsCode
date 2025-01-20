import sqlite3
import os

# Pastikan folder data ada
data_dir = 'src/data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Membuat atau membuka file database
conn = sqlite3.connect('src/data/snippet.db')
cursor = conn.cursor()

# Membuat tabel snippets jika belum ada
cursor.execute('''
CREATE TABLE IF NOT EXISTS snippets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language TEXT,
    utility TEXT,
    function TEXT,
    tags TEXT,
    code TEXT,
    description TEXT
)
''')

conn.commit()
conn.close()

print("Database and table 'snippets' created successfully!")
