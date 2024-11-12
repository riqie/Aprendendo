from repositoryDB import RepositoryDB

class BusinessRule:
    def __init__(self, repository: RepositoryDB):
        self.__repository = repository

    def calculateResults(self):
        data = self.__repository.searchData()
        
        if not data:
            print('Data not found. Check your connection to the DB.')
            
        else:
            answer = 0
            for item in data:
                answer += item
            print(f'Result: {answer}')

            
