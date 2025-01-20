import sqlite3

def create_snippet_db():
    db_path = 'src/data/snippet.db'  # Path ke database SQLite Anda
    conn = sqlite3.connect(db_path)  # Membuka koneksi ke database
    cursor = conn.cursor()

    # Memeriksa apakah tabel snippets ada, jika tidak, buat tabel baru
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS snippets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        language TEXT,
        utility TEXT,
        function TEXT,
        tags TEXT,
        code TEXT,
        description TEXT
    );
    ''')

    # Commit perubahan dan menutup koneksi
    conn.commit()
    conn.close()

    print("Database and table 'snippets' created successfully!")

# Menjalankan fungsi untuk membuat tabel snippets
create_snippet_db()
