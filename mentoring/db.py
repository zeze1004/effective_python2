class PostgresqlDBConnection:
    def __init__(self, url):
        self.client = postgresql_db
        # max_conn

    @classmethod
    def get_conn()
    def get_user_id(self, id):
        return self.client.sql(...)


# GET /profile/:id
def get_user_detail(id):
    conn = PostgresqlDBConnection("...")
    conn.get_user_id(id)

