import sqlite3


class SimpleSQLiteDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """Connect to the SQLite database."""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    # Implementing context management protocol
    def __enter__(self):
        """Called when entering the context (the 'with' block)."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Called when exiting the context (the 'with' block)."""
        self.close()

    def create_table(self, table_name, columns, uniques_var=None):
        """Create a new table in the database."""
        column_string = ", ".join(columns)
        if uniques_var is None:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_string})"
        else:
            unique_string = ", ".join(uniques_var)
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_string}, UNIQUE({unique_string}))"
        self.cursor.execute(query)

    def insert_data(self, table_name, data):
        """Insert data into the specified table."""
        placeholders = ", ".join(["?" for _ in data])
        query = f"INSERT OR IGNORE INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(query, data)
        self.conn.commit()

    def retrieve_data(self, table_name, columns=None):
        """Retrieve data from the specified table."""
        if columns is None:
            query = f"SELECT * FROM {table_name}"
        else:
            column_string = ", ".join(columns)
            query = f"SELECT {column_string} FROM {table_name}"

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()


class WikiPythonDB(SimpleSQLiteDB):
    def init_db(self):
        # Create PythonVersion table with columns (id, version)
        self.create_table(
            "PythonVersion", ["id INTEGER PRIMARY KEY", "version TEXT NOT NULL UNIQUE"]
        )

        # Create Category table with columns (id, name)
        self.create_table(
            "Category", ["id INTEGER PRIMARY KEY", "name TEXT NOT NULL UNIQUE"]
        )

        # Create Reference table with columns (id, url, python_version_id, category_id)
        self.create_table(
            "Reference",
            [
                "id INTEGER PRIMARY KEY",
                "url TEXT NOT NULL",
                "python_version_id INTEGER",
                "category_id INTEGER",
            ],
            uniques_var=["url", "python_version_id", "category_id"],
        )
        self.create_table(
            "ReferenceNoFragment",
            [
                "id INTEGER PRIMARY KEY",
                "url TEXT NOT NULL",
                "python_version_id INTEGER",
                "category_id INTEGER",
            ],
            uniques_var=["url", "python_version_id", "category_id"],
        )

    def get_id_by_name(self, table_name, column_name, value):
        """Retrieve the ID of a category based on its name."""
        query = f"SELECT id FROM {table_name} WHERE {column_name} = ?"
        self.cursor.execute(query, (value,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            raise Exception(f"{value} isn't in {column_name} of table {table_name}")

    def insert_data_python_wiki_db(
        self, python_version: str, category_name: str, reference_url: str
    ):
        self.insert_data("PythonVersion", (None, python_version))
        python_version_id = self.get_id_by_name(
            "PythonVersion", "version", python_version
        )
        self.insert_data("Category", (None, category_name))
        category_id = self.get_id_by_name("Category", "name", category_name)
        self.insert_data(
            "Reference", (None, reference_url, python_version_id, category_id)
        )

    def fetch_index(self, table_name, column_name, substring):
        query = f"SELECT * FROM {table_name} WHERE {column_name} LIKE '%{substring}%'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def delete_index(self, table_name, column_name, substring):
        query = f"DELETE FROM {table_name} WHERE {column_name} LIKE '%{substring}%'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def fetch_all_data(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result


def get_unique_row(db: WikiPythonDB):
    res = db.fetch_all_data("Reference")
    unique_row = set()
    for r in res:
        id, url, python_version, category_id = r
        path_segment = url.split("/")[-1]
        # print(path_segment)

        if "#" not in path_segment:
            unique_row.add((url, python_version, category_id))
        else:
            url_unique = url.split("#")[0]
            unique_row.add((url_unique, python_version, category_id))
    return unique_row


def db_python_doc():
    db = WikiPythonDB("WikiPython.db")
    with db:
        db.init_db()
        # res = db.delete_index("Reference", "url", "index")

        res = get_unique_row(db)
        for row in res:
            print(row)
            url, python_version, category_id = row
            db.insert_data(
                "ReferenceNoFragment", (None, url, python_version, category_id)
            )
        # for r in res:
        #    print(r)
        # print(db.retrieve_data("Category"))
        # db.insert_data_python_wiki_db(version, category_name, reference_url)


# def

# Example usage:
if __name__ == "__main__":
    db_python_doc()
    # create_db_for_python_doc()
