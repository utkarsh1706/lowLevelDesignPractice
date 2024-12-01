from connectionPool import ConnectionPooling

class ObjectPool:
    @staticmethod
    def run():
        pool = ConnectionPooling(5)

        c1 = pool.useConnection()
        c2 = pool.useConnection()

        c1.executeQuery("SELECT * FROM Student")
        c2.executeQuery("SELECT * FROM Subject")

        pool.releaseConnection(c1)


if __name__=="__main__":
    ObjectPool.run()