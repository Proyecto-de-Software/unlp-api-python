class Issue(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM issues"

        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def create(cls, data):
        sql = """
            INSERT INTO issues (email, description, category_id, status_id)
            VALUES (%s, %s, %s, %s)
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, list(data.values()))
        cls.db.commit()

        return True
