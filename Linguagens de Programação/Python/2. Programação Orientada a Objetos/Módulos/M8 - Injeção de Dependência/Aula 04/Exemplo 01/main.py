from connectorDB import ConnectorDB
from repositoryDB import RepositoryDB
from businessRule import BusinessRule

myConection = ConnectorDB()
myConection.connectToDB() #tente rodar o código sem esta linha

myRepository = RepositoryDB(myConection)

myBusinessRule = BusinessRule(myRepository)
myBusinessRule.calculateResults()