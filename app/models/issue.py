class Issue(object):
    @classmethod
    def all(cls, conn):
        sql = "SELECT * FROM issues"

        cursor = conn.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def create(cls, conn, data):
        sql = """
            INSERT INTO issues (email, description, category_id, status_id)
            VALUES (%s, %s, %s, %s)
        """

        cursor = conn.cursor()
        cursor.execute(sql, list(data.values()))
        conn.commit()

        return True
