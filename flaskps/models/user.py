class User(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM users'

        return cls.db.execute(sql).fetchall()

    @classmethod
    def create(cls, data):
        sql = """
            INSERT INTO users (email, password, first_name, last_name)
            VALUES (:email, :password, :first_name, :last_name)
        """

        cls.db.execute(sql, data)
        cls.db.commit()

        return True

    @classmethod
    def find_by_email_and_pass(cls, email, password):
        sql = """
            SELECT * FROM users AS u
            WHERE u.email = :email AND u.password = :password
        """
        return cls.db.execute(sql, (email, password)).fetchone()

