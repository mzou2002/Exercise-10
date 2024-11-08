import sqlite3
import pandas as pd

class Database:
    
    def __init__(self, csv_file):
        self.csv_file = csv_file
        
    def input_data(self):
        """
        Inputs csv file into database.
        
        Args:
        csv_file: csv file
        
        Return:
        New database 'books.dp' where you input csv_file.
        """
        books = pd.read_csv(self.csv_file)
        print(books)
        
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        
        create = '''CREATE TABLE books (
                    id INTEGER, title TEXT, author TEXT, year INTEGER
                    )'''
        cursor.execute(create)
        
        insert = '''INSERT INTO books VALUES (?,?,?,?)'''
        
        for index, row in books:
            cursor.executemany(insert, )
        
        read = '''SELECT title, author, year FROM books'''
        test = cursor.execute(read).fetchall()
        print(test)
        
if __name__ == "__main__":
    
    test = Database('books.csv')
    test.input_data()