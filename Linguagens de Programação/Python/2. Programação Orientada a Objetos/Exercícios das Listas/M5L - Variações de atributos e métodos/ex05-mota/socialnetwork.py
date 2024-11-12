'''5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa 
classe deve ter funcionalidades para adicionar amigos, publicar mensagens, 
comentar em posts e buscar por usuários.'''

class SocialNetwork:
    users = {}
    
    @classmethod
    def add_user(cls, username):
        cls.users[username] = {'friends': [], 'posts': []}
    
    @classmethod
    def add_friend(cls, username, friend):
        if friend in cls.users:
            cls.users[username]['friends'].append(friend)
        else:
            print('Not found.')
    
    def __init__(self, username):
        self.username = username
    
    def post_message(self, message):
        SocialNetwork.users[self.username]['posts'].append(message)
        print(message)

    def view_friends(self):
        print(SocialNetwork.users[self.username]['friends'])
    
    def view_posts(self):
        for post in SocialNetwork.users[self.username]['posts']:
            print(post)

    @staticmethod
    def get_all_users():
        return list(SocialNetwork.users.keys())

