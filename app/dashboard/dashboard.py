import sys
import os

# Menambahkan path untuk folder src ke sys.path agar Python dapat menemukan 'home'
src_path = os.path.join(os.path.dirname(__file__), '..', 'src')
sys.path.append(src_path)

def dashboard():
    print("Welcome to your dashboard!")

    while True:
        print("\n1. Add Snippet")
        print("2. View Snippets")
        print("3. Import Snippets from CSV")
        print("4. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            from home.add_snippet import add_snippet
            add_snippet()  # Panggil fungsi add_snippet tanpa parameter
        elif choice == '2':
            from home.view_snippets import view_snippets
            view_snippets()  # Panggil fungsi view_snippets
        elif choice == '3':
            from home.import_snippets import import_snippets
            import_snippets()  # Panggil fungsi import_snippets
        elif choice == '4':
            print("You have logged out.")
            break  # Keluar dari dashboard
        else:
            print("Invalid choice. Please try again.")
