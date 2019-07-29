class Issue(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM issues'

        return cls.db.execute(sql).fetchall()

    @classmethod
    def create(cls, data):
        sql = """
            INSERT INTO issues (email, description, category_id, status_id)
            VALUES (:email, :description, :category_id, :status_id)
        """

        cls.db.execute(sql, data)
        cls.db.commit()

        return True

