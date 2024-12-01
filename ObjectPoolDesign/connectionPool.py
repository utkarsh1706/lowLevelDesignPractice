from databaseConnection import DatabaseConnection

class ConnectionPooling:
    def __init__(self, n) -> None:
        self.numConnection = n
        self.inUse = set()
        self.connections = []
        self.createConnections(self.numConnection)

    def createConnections(self, num):
        for i in range(num):
            self.connections.append(DatabaseConnection(i))

    def releaseConnection(self, connection):
        if connection in self.inUse:
            self.inUse.remove(connection)
            self.connections.append(connection)

    def useConnection(self):
        if not self.connections:
            raise ValueError("No connections left")
        connection = self.connections.pop()
        self.inUse.add(connection)
        return connection
