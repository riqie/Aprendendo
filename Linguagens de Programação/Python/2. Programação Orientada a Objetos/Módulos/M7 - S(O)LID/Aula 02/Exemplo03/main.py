from artist import Artist
from circus import Circus

myClown = Artist('Clown')
myJuggler = Artist('Juggler')
myCircus = Circus()

myCircus.presentShow(myClown)
print()
myCircus.presentShow(myJuggler)