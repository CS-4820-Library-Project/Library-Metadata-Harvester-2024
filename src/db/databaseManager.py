import sqlite3
import os
import sys

class DatabaseManager:

    def __init__(self, db_name='metadata.sqlite', db_path=None):
        if not getattr(sys, 'frozen', False):
            application_path = os.path.dirname(os.path.abspath(__file__))
            self.db_path = os.path.join(application_path, db_name)
        else:
            self.db_path = os.path.join(db_path, db_name)

    def execute_query(self, query, params=(), fetch=False):
        """General purpose method to execute database queries."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(query, params)
                if fetch:
                    return cursor.fetchall()
                conn.commit()
            except sqlite3.Error as e:
                print(f"Database error: {e}")
            except Exception as e:
                print(f"Exception in query execution: {e}")

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.execute_query(query)

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.execute_query(query, data)

    def fetch_data(self, table_name, condition=''):
        query = f"SELECT * FROM {table_name} {condition}"
        return self.execute_query(query, fetch=True)

    def update_data(self, table_name, update_values, condition):
        query = f"UPDATE {table_name} SET {update_values} WHERE {condition}"
        self.execute_query(query)

    def delete_data(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_query(query)

    def data_exists(self, table_name, condition):
        """Check if data exists in the table matching the condition."""
        result = self.fetch_data(table_name, f"WHERE {condition}")
        return result is not None and len(result) > 0

