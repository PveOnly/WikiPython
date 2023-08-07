import random
import sqlite3

import pandas as pd
from flask import Flask, jsonify, render_template_string

# Fix seed
random.seed(1)

from src.database.simple_database import SimpleSQLiteDB

# Create a Flask app
app = Flask(__name__)


class SimpleDatabaseView(SimpleSQLiteDB):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.tables_name = self.get_table_names()

    @property
    def table_names(self):
        return self.tables_name

    def get_table_names(self):
        with self:
            cursor = self.conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            table_names = [row[0] for row in cursor.fetchall()]
        return table_names

    def get_database_head(self, table_name="Reference", number_row=25):
        with self:
            cursor = self.conn.cursor()
            cursor.execute(
                f"SELECT * FROM {table_name} LIMIT {number_row}"
            )  # Replace your_table_name with the actual table name in your database
            head_data = cursor.fetchall()
            return head_data, cursor

    def get_random_url(self, table_name="ReferenceNoFragment"):
        with self:
            cursor = self.conn.cursor()
            cursor.execute(
                f"SELECT * FROM {table_name}"
            )  # Replace your_table_name with the actual table name in your database
            head_data = cursor.fetchall()
            result = random.choice(head_data)
            return result


@app.route("/")
def show_head():
    head_data = db.table_names
    return jsonify(head_data)


@app.route("/pandas/random")
def get_random_python_url():
    random_url = db.get_random_url()
    return jsonify(random_url)


@app.route("/pandas/<string:table_name>/<int:number_row>")
@app.route("/pandas/<string:table_name>/")
def show_head_pandas(table_name, number_row=25):
    if table_name not in db.tables_name:
        return f"Table '{table_name}' not found in the database."
    head_data, cursor = db.get_database_head(table_name, number_row)
    columns = [description[0] for description in cursor.description]
    # df = pd.DataFrame(head_data, columns=columns)
    head_data.insert(0, columns)
    return jsonify(head_data)


@app.route("/test/simple")
def test_url():
    head_data = db.table_names
    return jsonify(head_data)


if __name__ == "__main__":
    db = SimpleDatabaseView("WikiPython.db")
    app.run(debug=True)
