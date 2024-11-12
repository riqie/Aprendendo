class Smartphone:
    def __init__(self, model):
        self.__model = model

    def sendMessage(self, message):
        print(f'Sending message: {message}')

    def verifyEmails(self):
        print('Checking e-mails...')

    def watchYoutube(self):
        print('Watching Youtube...')
        