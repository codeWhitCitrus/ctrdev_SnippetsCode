import csv
import sqlite3

def import_snippets():
    print("\nImport Snippets")
    csv_file = input("Enter the path to the CSV file: ")

    try:
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row jika ada

            # Buka koneksi ke database
            conn = sqlite3.connect('src/data/snippet.db')
            cursor = conn.cursor()

            # Insert data dari CSV ke dalam database
            for row in csv_reader:
                cursor.execute('''
                INSERT INTO snippets (language, utility, function, tags, code, description) 
                VALUES (?, ?, ?, ?, ?, ?)
                ''', (row[0], row[1], row[2], row[3], row[4], row[5]))

            conn.commit()
            conn.close()
            print("Snippets imported successfully!")

    except Exception as e:
        print(f"Error: {e}")
