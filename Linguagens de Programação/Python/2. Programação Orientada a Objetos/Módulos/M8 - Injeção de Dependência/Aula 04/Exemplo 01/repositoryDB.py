from connectorDB import ConnectorDB

class RepositoryDB:
    def __init__(self, connector: ConnectorDB):
        self.__connector = connector

    def searchData(self):
        if self.__connector.connection:
            return [1,2,3,4,5]
        return None