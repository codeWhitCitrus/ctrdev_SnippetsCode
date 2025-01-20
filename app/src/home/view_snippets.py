from tabulate import tabulate
import sqlite3

def view_snippets():
    print("\nView Snippets")
    # Ambil data snippets dari database
    conn = sqlite3.connect('src/data/snippet.db')
    cursor = conn.cursor()

    # Query untuk mengambil data dari tabel snippets
    cursor.execute("SELECT * FROM snippets")
    snippets = cursor.fetchall()

    if snippets:
        # Tentukan header tabel
        headers = ['ID', 'Language', 'Utility', 'Function', 'Tags', 'Code', 'Description']
        
        # Tampilkan tabel dengan tabulate
        print(tabulate(snippets, headers=headers, tablefmt='grid'))
    else:
        print("No snippets found.")

    conn.close()
