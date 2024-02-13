import csv
import sqlite3

def generate_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Age', 'Place']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
def load_csv_to_sqlite(filename, tablename):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {tablename} (Name TEXT, Age INT, Place TEXT)")
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute(f"INSERT INTO {tablename} (Name, Age, Place) VALUES (?, ?, ?)",
                           (row['Name'], row['Age'], row['Place']))
    conn.commit()
    conn.close()
def display_data_from_sqlite(tablename, limit=6):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tablename} LIMIT ?", (limit,))
    for row in cursor.fetchall():
        print(row)

    conn.close()
def main():
    csv_filename = 'data.csv'
    sqlite_tablename = 'data_table'


    static_data = [
        {'Name': 'Noor', 'Age': 51, 'Place': 'Azerbaijan'},
        {'Name': 'Saba', 'Age': 31, 'Place': 'India'},
        {'Name': 'Alina', 'Age': 67, 'Place': 'Los Angeles'},
        {'Name': 'Bobby', 'Age': 53, 'Place': 'Chicago'},
        {'Name': 'fathe', 'Age': 41, 'Place': 'France'},
        {'Name': 'miny', 'Age': 21, 'Place': 'China'},
    ]
    generate_csv(csv_filename, static_data)
    load_csv_to_sqlite(csv_filename, sqlite_tablename)
    print("First 6 records loaded from SQLite:")
    display_data_from_sqlite(sqlite_tablename)
if __name__ == "__main__":
    main()