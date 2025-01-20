import sqlite3

def add_snippet():
    print("\nAdd Snippet")
    
    # Meminta input pengguna
    language = input("Enter the programming language: ")
    utility = input("Enter the utility: ")
    function = input("Enter the function: ")
    tags = input("Enter tags (separated by commas): ")
    code = input("Enter the code: ")
    description = input("Enter the description: ")
    
    # Simpan snippet ke database SQLite
    try:
        # Koneksi ke database
        conn = sqlite3.connect('src/data/snippet.db')  # Ganti dengan path yang sesuai
        cursor = conn.cursor()

        # Membuat table jika belum ada
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

        # Menyimpan snippet ke database
        cursor.execute('''
            INSERT INTO snippets (language, utility, function, tags, code, description) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (language, utility, function, tags, code, description))

        conn.commit()
        conn.close()
        print("Snippet added successfully!")

    except Exception as e:
        print(f"Error: {e}")

    # Setelah selesai menambah snippet, kembali ke dashboard
    return_to_dashboard()

def return_to_dashboard():
    choice = input("Do you want to go back to the dashboard? (y/n): ")
    if choice.lower() == "y":
        from dashboard.dashboard import dashboard
        dashboard()  # Kembali ke dashboard
    else:
        print("Exiting the application.")
        exit()  # Keluar aplikasi
