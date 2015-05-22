import sqlite3


class Database:

    comment_table = 'editables'

    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self._create()

    def _create(self):
        """ Creates the necessary tables if they do not exists """
        cursor = self.connection.cursor()
        query = (
            'CREATE TABLE IF NOT EXISTS {} '
            '(id TEXT PRIMARY KEY)'
        ).format(Database.comment_table)
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def store_editable(self, editable):
        """ Stores the editable id in the database

        To prevent the bot from revisiting comments,
        save the parsed editable id in the database.

        Args:
            editable: PRAW comment, submission or message
        """
        cursor = self.connection.cursor()
        query = 'INSERT INTO {} VALUES (?)'.format(Database.comment_table)
        cursor.execute(query, (editable.id,))
        self.connection.commit()
        cursor.close()

    def get_editable(self, editable):
        """ Gets the values of editable stored in the database

        Args:
            editable: PRAW comment, submission or message
        Returns:
            If editable exists:
                A tuple of the data in the columns
            Otherwise:
                None
        """
        cursor = self.connection.cursor()
        query = 'SELECT * FROM {} WHERE id = ?'.format(Database.comment_table)
        cursor.execute(query, (editable.id,))
        row = cursor.fetchone()
        cursor.close()
        return row
