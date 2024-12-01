class DatabaseConnection:
    def __init__(self, id) -> None:
        self.connectionID = id

    def executeQuery(self, query):
        print(f"Executing Query {query} on connectionID: {self.connectionID}")
        return