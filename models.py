TABLENAME = "TODO"
import sqlite3 as sqlite3
class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()

    def create_to_do_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "ToDo" (
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Description TEXT,
        _is_done boolean,
        _is_deleted boolean,
        CreatedOn Date DEFAULT CURRENT_DATE,
        DueDate Date,
        UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """
        self.conn.execute(query)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
        id INTEGER PRIMARY KEY,
        Name TEXT,
        CreatedOn Date DEFAULT CURRENT_DATE
        );
        """
        self.conn.execute(query)

class ToDoModel:

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description):
        query = f'insert into {TABLENAME} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}")'

        result = self.conn.execute(query)
        return 'OK'

    def select(self, text):
        query = f'select * ' \
                f'from {TABLENAME} ' \
                f'where Title = "{text}"'

        result = self.conn.execute(query)
        return 'OK'

    def delete(self, text):
        query = f'delete from {TABLENAME} ' \
                f'where Title = "{text}"'

        result = self.conn.execute(query)
        return 'OK'

    def update(self, text, description):
        query = f'update {TABLENAME} ' \
                f'set Description = "{description}" ' \
                f'where Title = "{text}" '

        result = self.conn.execute(query)
        return 'OK'
