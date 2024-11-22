'''5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa 
classe deve ter funcionalidades para adicionar amigos, publicar mensagens, 
comentar em posts e buscar por usuários.'''

from socialnetwork import SocialNetwork

def main():
    #Adicionando usúarios
    SocialNetwork.add_user('joao')
    joao = SocialNetwork('joao')

    SocialNetwork.add_user('leo')
    leo = SocialNetwork('leo')

    SocialNetwork.add_user('rafael')
    rafael = SocialNetwork('rafael')

    #Adicionando e printando lista de amigos
    SocialNetwork.add_friend('rafael', 'leo')
    rafael.view_friends()

    #Postando mensagens e visualizando
    rafael.post_message('Hello, world!')
    rafael.post_message('I love football')

    leo.post_message('Vai Palmeiras!')

    SocialNetwork.get_all_users()
main()


#rafael.view_posts()
#leo.view_posts()
