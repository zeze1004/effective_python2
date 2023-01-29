class TestClass:
    db_conn = None
    def __init__(self):
        self.tmp1 = 1
        self.tmp2 = 2
        self.test = []

    def hello(self):
        pass

    @classmethod
    def print(cls, msg):
        cls.test.append(msg)
        print(msg)

    def query(self, qString):
        client = get_conn("...")
        client.request_query("...")

    @classmethod
    def get_conn(cls, url):
        if cls.db_conn:
           return cls.db_conn
        db_conn = get_postgresql_db_conn(url)
        return db_conn


    @staticmethod
    def get_conn(url):
        if db_conn:
           return db_conn
        db_conn = get_postgresql_db_conn(url)
        return db_conn


    def printSelf(self, msg):
        self.test.append(msg)

if __name__ == "__main__":
    a = TestClass()
    b = TestClass()

    # Immutable -> Functional
    # Functional vs. Object-oriented.

    print("hello")
    b.printSelf("hello b")
    a.printSelf("hello a")

    print(a.test)
    print(b.test)
    print(TestClass.test)

    #TestClass.print("hello")

